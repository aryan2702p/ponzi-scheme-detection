

import pandas as pd
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import re

model = load_model("conv1d_model.h5")

# Load the tokenizer from file
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

def preprocess_opcode(opcode_string, tokenizer, max_sequence_length):
    opcodes = re.findall(r'\b[A-Z0-9]+(?=\s|$)', opcode_string)  
    sorted_opcodes = sorted(set(opcodes))  
    opcode_modified = ' '.join(sorted_opcodes) 
    opcode_sequence = tokenizer.texts_to_sequences([opcode_modified])  
    opcode_sequence_padded = pad_sequences(opcode_sequence, maxlen=max_sequence_length) 
    return opcode_sequence_padded


opcode_file = "subset_file.csv" 
smart_contract_df = pd.read_csv(opcode_file)
opcodes = smart_contract_df['opcode'].values.tolist()  # Convert to list
    
max_sequence_length=100 # can be changed
predictions = []

for opcode in opcodes:
    preprocessed_input = preprocess_opcode(opcode, tokenizer, max_sequence_length)
    prediction = model.predict(preprocessed_input)
    predictions.append(prediction)
    is_ponzi = prediction > 0.3
    result = ["Ponzi scheme" if ponzi else "Not a Ponzi scheme" for ponzi in is_ponzi]
    print(result)
    print(prediction)


        
    
   


