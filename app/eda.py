import numpy as np
import pandas as pd


def preprocess_data() -> pd.DataFrame:
    df_clients = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_clients.csv')
    df_close_loan = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_close_loan.csv')
    df_job = pd.read_csv('https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_job.csv')
    df_last_credit = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_last_credit.csv')
    df_loan = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_loan.csv')
    df_pens = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_pens.csv')
    df_salary = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_salary.csv')
    df_target = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_target.csv')
    df_work = pd.read_csv(
        'https://raw.githubusercontent.com/aiedu-courses/stepik_linear_models/main/datasets/D_work.csv')

    df_clients = df_clients.rename(columns={'ID': 'ID_CLIENT'})
    df = pd.merge(df_target, df_clients, on='ID_CLIENT', how='left')
    df = pd.merge(df, df_salary, on='ID_CLIENT', how='left')

    loans = df_loan.merge(df_close_loan, on='ID_LOAN')
    aggregated_df = loans.groupby('ID_CLIENT').agg(LOAN_NUM_TOTAL=('ID_LOAN', 'count'),
                                                   LOAN_NUM_CLOSED=('CLOSED_FL', 'sum')).reset_index()
    df = pd.merge(df, aggregated_df, on='ID_CLIENT', how='left')

    df = df.drop(
        ['FAMILY_INCOME', 'MARITAL_STATUS', 'REG_ADDRESS_PROVINCE', 'FACT_ADDRESS_PROVINCE', 'POSTAL_ADDRESS_PROVINCE',
         'EDUCATION', 'ID_CLIENT'], axis=1)
    df = df.drop_duplicates()
    df = df.dropna()

    return df
