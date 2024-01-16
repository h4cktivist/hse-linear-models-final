import requests
import json
import pandas as pd


def get_data():
    URL = 'http://127.0.0.1:8000/get-data'
    res = requests.get(URL)
    df = pd.json_normalize(res.json())
    return df


def make_prediction(data):
    URL = 'http://127.0.0.1:8000/predict'
    res = requests.post(URL, json=data)
    if res.status_code != 200:
        return None
    return res.json()['pred'], res.json()['proba']
