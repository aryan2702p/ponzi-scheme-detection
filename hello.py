from flask import Flask
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
#from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import re
app = Flask(__name__)

model = load_model("test_model1.h5")

def preprocess_opcode(opcode_string, tokenizer, max_sequence_length):
    opcodes = re.findall(r'\b[A-Z0-9]+(?=\s|$)', opcode_string)  
    sorted_opcodes = sorted(set(opcodes))  
    opcode_modified = ' '.join(sorted_opcodes) 
    opcode_sequence = tokenizer.texts_to_sequences([opcode_modified])  
    opcode_sequence_padded = pad_sequences(opcode_sequence, maxlen=max_sequence_length) 
    return opcode_sequence_padded

@app.route('/')
def index():
    try:
        opcode_file = "smart_contract.csv"
        smart_contract_df = pd.read_csv(opcode_file)
        opcodes = smart_contract_df['opcode'].values.tolist()  # Convert to list
    
        tokenizer = Tokenizer()  # Use a fresh tokenizer
        max_sequence_length=65 # can be changed
        predictions = []
        for opcode in opcodes:
            preprocessed_input = preprocess_opcode(opcode, tokenizer, max_sequence_length)
            prediction = model.predict(preprocessed_input)
            predictions.append(prediction)

        is_ponzi = prediction > 0.5
        result = ["Ponzi scheme" if ponzi else "Not a Ponzi scheme" for ponzi in is_ponzi]
        html_content = f"<html><body><p>Prediction: {prediction}</p><br>{result}</body></html>"
            
        return html_content
    
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run()
