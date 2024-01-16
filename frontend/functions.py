import requests
import json
import pandas as pd


def get_data():
    URL = 'https://hse-linear-models.onrender.com/get-data'
    res = requests.get(URL)
    df = pd.json_normalize(res.json())
    return df


def make_prediction(data):
    URL = 'https://hse-linear-models.onrender.com/predict'
    res = requests.post(URL, json=data)
    if res.status_code != 200:
        return None
    return res.json()['pred'], res.json()['proba']
