from fastapi import FastAPI, File, UploadFile
import uvicorn
import prediction

app = FastAPI()

@app.get('/index')
def hello_world():
    return "hello world"

@app.post('/api/predict')
def predict_image(file: UploadFile = File(...)):
    sport_name = prediction.identify_sport(file)

    return sport_name

if __name__ == '__main__':
    uvicorn.run(app, port=8080 ,host='0.0.0.0')