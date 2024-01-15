from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from pickle import load

import json

from db.init import SessionLocal
from db.schemas import RecordSchema, UserDataSchema
from db.models import Record


app = FastAPI()


def get_session() -> Session:
    with SessionLocal() as session:
        return session


def load_model():
    with open('model.pickle', 'rb') as f:
        model = load(f)
    return model


@app.get('/get-data', response_model=List[RecordSchema])
async def get_data(limit: int = 10, db: Session = Depends(get_session)):
    return db.query(Record).limit(limit).all()


@app.post('/predict')
async def make_prediction(df: UserDataSchema, db: Session = Depends(get_session)):
    model = load_model()

    df = pd.DataFrame(df.model_dump(), index=[0])
    df.columns = map(str.upper, df.columns)

    probs = model.predict_proba(df)
    classes = probs[:, 1] > 0.4742448484764867

    result_classes = {
        False: 'Скорее всего, клиент даст негативный ответ на предложение банка.',
        True: 'Скорее всего, клиент согласится на предложение банка.'
    }
    prediction = result_classes[classes[0]]

    return {
        'pred': prediction,
        'proba': probs[:, 1][0]
    }
