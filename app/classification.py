from pickle import load

import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler

from eda import preprocess_data

df = preprocess_data()
ss = StandardScaler()
ss.fit(df.drop(['AGREEMENT_RK', 'TARGET'], axis=1))


def load_model():
    with open('app/model.pickle', 'rb') as f:
        model = load(f)

    return model


def make_prediction(df: pd.DataFrame):
    model = load_model()

    df = pd.DataFrame(ss.transform(df), columns=df.columns)
    probs = model.predict_proba(df)
    classes = probs[:, 1] > 0.4742448484764867

    result_classes = {
        False: 'Скорее всего, клиент даст негативный ответ на предложение банка.',
        True: 'Скорее всего, клиент согласится на предложение банка.'
    }
    prediction = result_classes[classes[0]]

    return prediction, probs[:, 1][0]
