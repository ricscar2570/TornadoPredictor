
import pandas as pd
import requests

def fetch_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore API: {response.status_code}")
        return {}

def validate_data(data):
    required_fields = ['main', 'wind', 'weather']
    for field in required_fields:
        if field not in data:
            print(f"Campo mancante: {field}")
            return None
    return data

def save_data_to_csv(data, output_path):
    df = pd.DataFrame([data])
    df.to_csv(output_path, index=False)
    print(f"Dati salvati in: {output_path}")
