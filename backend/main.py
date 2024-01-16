from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
import pickle

from db.init import SessionLocal
from db.schemas import RecordSchema, UserDataSchema
from db.models import Record


app = FastAPI()


def get_session() -> Session:
    with SessionLocal() as session:
        return session


def load_model() -> LogisticRegression:
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)
    return model


def get_dataset() -> pd.DataFrame:
    db = get_session()
    data = [r.as_dict() for r in db.query(Record).all()]
    df = pd.DataFrame(data).drop(['id'], axis=1)
    df.columns = map(str.upper, df.columns)
    return df


def scale_data(df: pd.DataFrame) -> pd.DataFrame:
    data = get_dataset().drop(['TARGET'], axis=1)
    ss = StandardScaler()
    ss.fit(data)
    df = pd.DataFrame(ss.transform(df), columns=df.columns)
    return df


def get_best_model(X: pd.DataFrame, y: np.array) -> LogisticRegression:
    model = LogisticRegression()
    params = {
        'C': np.logspace(-5, 5, 100),
    }

    search = RandomizedSearchCV(
        model,
        param_distributions=params,
        n_iter=5,
        cv=5
    )
    search.fit(X, y)
    return search.best_estimator_


@app.get('/get-data', response_model=List[RecordSchema])
async def get_data(limit: int = 10, db: Session = Depends(get_session)) -> list:
    return db.query(Record).limit(limit).all()


@app.post('/predict')
async def make_prediction(df: UserDataSchema, db: Session = Depends(get_session)) -> dict:
    model = load_model()

    df = pd.DataFrame(df.model_dump(), index=[0])
    df.columns = map(str.upper, df.columns)
    df = scale_data(df)

    probs = model.predict_proba(df)
    classes = probs[:, 1] > 0.4742448484764867

    result_classes = {
        False: 'Скорее всего, клиент даст негативный ответ на предложение банка.',
        True: 'Скорее всего, клиент согласится на предложение банка.'
    }
    prediction = result_classes[classes[0]]
    print(prediction, probs[:, 1][0])

    return {
        'pred': prediction,
        'proba': probs[:, 1][0]
    }


@app.get('/fit')
def fit_model() -> dict:
    df = get_dataset()
    X = scale_data(df.drop(['TARGET'], axis=1))
    y = df['TARGET']
    model = get_best_model(X, y)
    with open('model_new.pickle', 'wb') as f:
        pickle.dump(model, f)
    return {
        'message': 'Success'
    }
