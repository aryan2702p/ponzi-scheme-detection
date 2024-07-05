import requests

def get_contract_bytecode(contract_address, api_key):
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getCode&address={contract_address}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['result']

def save_to_file(opcodes, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(opcodes))

def to_opcode(bytecode):
    opcodes = []
    for i in range(0, len(bytecode), 2):
        byte = bytecode[i:i+2]
        opcodes.append(byte)
    
    return opcodes

contract_address = "0x582b2489710a4189ad558b6958641789587fcc27"  
api_key = "ZCYE4GPU35H428VR52TYAR5C9RHZIJKVUZ"  
bytecode = get_contract_bytecode(contract_address, api_key)

save_to_file(bytecode, "bytecode_output.txt")

opcode=to_opcode(bytecode)
save_to_file(opcode, "opcode_output.txt")


