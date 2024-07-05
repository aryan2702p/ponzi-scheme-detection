import re
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model

model = load_model("test_model1.h5")  

tokenizer = Tokenizer()

def preprocess_opcode(opcode_string, tokenizer, max_sequence_length):
    opcodes = re.findall(r'\b[A-Z0-9]+(?=\s|$)', opcode_string)  
    sorted_opcodes = sorted(set(opcodes))  
    opcode_modified = ' '.join(sorted_opcodes) 
    opcode_sequence = tokenizer.texts_to_sequences([opcode_modified])  
    opcode_sequence_padded = pad_sequences(opcode_sequence, maxlen=max_sequence_length) 
    return opcode_sequence_padded


max_sequence_length=65 # can be changed
input_opcode = "" ## will bw getting from user via frontend
preprocessed_input = preprocess_opcode(input_opcode, tokenizer, max_sequence_length)


prediction = model.predict(preprocessed_input)


print(prediction)
