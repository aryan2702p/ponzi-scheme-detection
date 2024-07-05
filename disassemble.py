import subprocess

def compile_contract(contract_file):
    try:
        # Compile the contract using solc
        output = subprocess.check_output(["solc", "--bin-runtime", contract_file]).decode("utf-8")
        return output.split("Binary:")[1].strip()
    except subprocess.CalledProcessError as e:
        print("Error compiling contract:", e)
        return None

def disassemble_bytecode(bytecode):
  
    try:
        # Disassemble the bytecode using solc
        output = subprocess.check_output(["solc", "--opcodes"], input=bytecode.encode("utf-8")).decode("utf-8")
        return output.strip()
    except subprocess.CalledProcessError as e:
        print("Error disassembling bytecode:", e)
        return None

def save_opcodes(opcodes, output_file):
    """
    Save the opcodes to a file.
    """
    try:
        # Save opcodes to file
        with open(output_file, "w") as f:
            f.write(opcodes)
        print("OpCodes saved to", output_file)
    except IOError as e:
        print("Error saving opcodes:", e)

def main():
    contract_file = "YourContract.sol"
    output_file = "opcodes.txt"

    # Compile the contract
    bytecode = compile_contract(contract_file)
    if bytecode is None:
        return

    # Disassemble bytecode to obtain opcodes
    opcodes = disassemble_bytecode(bytecode)
    if opcodes is None:
        return

    # Save opcodes to file
    save_opcodes(opcodes, output_file)

if __name__ == "__main__":
    main()
