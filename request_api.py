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


def parse_json(json_data, attribute):
    valores = []
    for item in json_data['data']:
        valores.append([item['attributes']['date'], item['attributes'][attribute]])
    
    valores = pd.DataFrame(valores, columns=['date', attribute])

    if attribute == 'net_asset_value':
        # valores[attribute] = valores[attribute].astype(float)
        pass

    return valores


def calculate_roi(df):
    first_value = df['net_asset_value'].iloc[0]
    last_value = df['net_asset_value'].iloc[-1]
    retorno = (last_value - first_value)/first_value
    return retorno