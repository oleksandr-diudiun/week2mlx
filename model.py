from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/get-prediction")
def getPrediction(title):
    #run funtion to call model
    return None