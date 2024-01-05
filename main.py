from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks


app = FastAPI()


from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

@app.get("/predict/{input_data}")
def predict(input_data: str):
    # Add your data science prediction code here
    prediction = "Your prediction: " + input_data
    return {"prediction": prediction}
