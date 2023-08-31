import numpy as np
import pandas as pd
import requests

def ask_api_real_assets(id:str, from_date: str, to_date: str):

    url = 'https://fintual.cl/api/real_assets/'

    data_to_ask= {
        'from_date': from_date,
        'to_date': to_date
    }
    response = requests.get(url + id + '/days?', data=data_to_ask)
    print(f'Status Code: {response.status_code}')

    return response


def parse_json(json_data, attribute='net_asset_value'):
    df = pd.json_normalize(json_data['data'])
    df = df[['attributes.date', 'attributes.' + attribute]]
    return df


def calculate_roi(df, attribute='net_asset_value'):
    first_value = df['attributes.' + attribute].iloc[0]
    last_value = df['attributes.' + attribute].iloc[-1]
    roi = (last_value - first_value)/first_value
    return roi