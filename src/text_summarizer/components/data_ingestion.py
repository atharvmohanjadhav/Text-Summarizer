import os
import zipfile
from urllib import request
from src.text_summarizer.logging_info import logger
from src.text_summarizer.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def dowload_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name,header = request.urlretrieve(url=self.config.source_URL,filename=self.config.local_data_file)
            logger.info(f"FIle downloaded sucessfully!")
        else:
            logger.info(f"file already exsit!")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_dir:
            zip_dir.extractall(unzip_path)