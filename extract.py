import os
import json
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
filename = f'{data_dir}/{timestamp}.json'

url='https://api.tfl.gov.uk/BikePoint/'

response = requests.get(url)

data = response.json()

with open(filename,'w') as file:
    json.dump(data, file)