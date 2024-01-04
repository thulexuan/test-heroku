from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


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