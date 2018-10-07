import json
import requests
import pandas, numpy

API_KEY = 'W861UNACY4UTLWP3'

def get_daily_data(symbol: str):
    response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}')
    return response.json()['Time Series (Daily)']

