import os
import time
import json
import requests 
from dotenv import load_dotenv
from db_client import DatabaseClient
from db_config import API_TRIAL_THRESHOLD
load_dotenv('../../.env')

class BaseEtl():

    def __init__(self, source_system, url, db_client=None):
        self.database = db_client or DatabaseClient()
        self._load_tries_count = 0
        self.source_system = source_system
        self.url = url

    def run(self):
        watermark_value = self.database.get_watermark_value(self.source_system)
        while(self._load_tries_count < API_TRIAL_THRESHOLD):
            try:
                json_data = self._get_data(self.url, watermark_value)
                self.database.load_to_db(json_data)
                print('Data loaded successfully')
                return
            except (ConnectionError, TimeoutError, requests.HTTPError) as error:
                print(f'Error occured while loading: {error}')
                self._load_tries_count += 1
                self.save_failed_load(str(error))
                if(self._load_tries_count < API_TRIAL_THRESHOLD):
                    print(f'Retrying the Load..... [{self._load_tries_count} / {API_TRIAL_THRESHOLD}]')
                    time.sleep(4)
                else:
                    print(f'Error occured while loading: {error}')
                    print('Number of trials exceeded the allowed threshold')


    def save_failed_load(self, error_message):
        self.database.load_to_control_table(error_message)

    def _get_data(self, url, watermark):
        parameteres = {
            "part" : "snippet",
            "type" : "playlist",
            "q" : "music",
            "key" : os.getenv("YOUTUBE_API_KEY")
        }
        response = requests.get(url, params=parameteres)
        response.raise_for_status()
        return response.json()
    
if __name__ == '__main__':
    etl = BaseEtl(source_system='SAP_ERP', url='https://www.googleapis.com/youtube/v3/search')
    etl.run()