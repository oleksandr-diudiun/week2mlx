from fastapi import FastAPI 
import sentencepiece as spm
import torch.nn as nn
#from week2_Alex.ipynb import dataframe_sentence_generator, 

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/get-prediction")
def getPrediction(title):

    #tokenize the title
    sp = spm.SentencePieceProcessor()
    sp.load('spm_Alex_week2.model')
    sp.encode_as_pieces(title)

    #2. Run the tokens through Word2Vec&take the average
    
    #3. Run the resulting method through our regression model
    return prediction