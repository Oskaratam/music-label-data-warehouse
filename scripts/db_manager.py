import os 
import pyodbc
from dotenv import load_dotenv

class DatabaseManager:
    def __init__(self):
        load_dotenv('.env')
        self.SERVER_NAME = os.getenv('SERVER_NAME')
        self.DATABASE_NAME = os.getenv('DATABASE_NAME')
        self.UID = os.getenv('UID')
        self.PASSWORD = os.getenv('PASSWORD')
    
    def load_to_db(self, raw_data, source_system, source_url=None):
        connection = self.__connect_to_db()
        cursor = connection.cursor()
        watermark = self._get_watermark_value
        


        print('Loaded to db')
        connection.close()


    def _load_to_control_table():
        print()
        

    def _get_watermark_value(connection, source_system):
        print()
        

    def load_json(watermark=None):
        print()

    def load_html(watermark=None):
        print()

    def  _connect_to_db(self) -> pyodbc.Connection:
        try:
            connection = pyodbc.connect(
                f'DRIVER={{ODBC Driver 18 for SQL Server}};'
                f'SERVER={self.SERVER_NAME};'
                f'DATABASE={self.DATABASE_NAME};'
                f'UID={self.UID};' 
                f'PWD={self.PASSWORD};'
                'TrustServerCertificate=yes;'
            )  
            return connection
        except pyodbc.Error as e:
            print('!!!!!!!!!!!!!!!!!')
            print(f'Connection to the database failed \n Error Message: {e}')






