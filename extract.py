import os
import json
import time
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
filename = f'{data_dir}/{timestamp}.json'

url='https://api.tfl.gov.uk/BikePoint/'

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    response = requests.get(url)
    status_code = response.status_code

    if 200<= status_code <300:
        data = response.json()

        with open(filename,'w') as file:
            json.dump(data, file)

        print(f'File {filename} saved successfully 🎉')

        break

    elif 300<= status_code <500:
        print(f'API call failed, status code {status_code} 😬')
        break

    else:
        if attempt == max_attempts:
            print(f'Max number of attempts reached. Status code {status_code}. Investigate further.')
        else:
            print(f'Attempt {attempt} failed, status code {status_code}. Trying again 😅')
        
        attempt+=1
        time.sleep(30)

