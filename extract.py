import os
import json
import time
import logging
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
logger.info('Logger was successfully intialised.')

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
        try:
            data = response.json()
            with open(filename,'w') as file:
                json.dump(data, file)
            print(f'File {filename} saved successfully 🎉')
            logger.info(f'File {filename} saved successfully 🎉')
        except Exception as e:
            print(f'An error occurred when saving the JSON: {e}')
            logger.error(f'An error occurred when saving the JSON: {e}')
        
        break

    elif 300<= status_code <500:
        print(f'API call failed, status code {status_code} 😬')
        logger.error(f'API call failed, status code {status_code} 😬')
        break

    else:
        if attempt == max_attempts:
            print(f'Max number of attempts reached. Status code {status_code}. Investigate further.')
            logger.warning(f'Max number of attempts reached. Status code {status_code}. Investigate further.')
        else:
            print(f'Attempt {attempt} failed, status code {status_code}. Trying again 😅')
            logger.error(f'Attempt {attempt} failed, status code {status_code}. Trying again 😅')
        
        attempt+=1
        time.sleep(30)

