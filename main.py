from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import joblib

app = FastAPI()

@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import joblib

app = FastAPI()

@app.get("/prediction/", tags=["Prediction"])
def get_prediction(review: str):
    """
    Endpoint to get sentiment prediction for a review text.
    """
    vectorizer = joblib.load("/usercode/vectorizer.joblib")
    model = joblib.load('/usercode/model.pkl')
    data = vectorizer.transform([review])
    response =  model.predict(data)
    sentiments = ['negative', 'neutral', 'positive']
    return sentiments[response[0] + 1]

@app.get("/", tags=["Documentation"])
async def docs_redirect():
    """
    Redirect to FastAPI documentation.
    """
    response = RedirectResponse(url='/docs')
    return response


