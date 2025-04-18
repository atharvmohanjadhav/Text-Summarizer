from src.text_summarizer.constants import *
from src.text_summarizer.utils.common import read_yaml, create_dir
from src.text_summarizer.entity import DataIngestionConfig,DataTransformationConfig
from src.text_summarizer.exception.exception import SummaryException
import sys

class ConfigurationManager:
    def __init__(self,config_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(path_to_yaml=config_path)
        self.params = read_yaml(path_to_yaml=params_file_path)

        create_dir([self.config.artifacts_root])

    def get_data_ingesion_config(self)-> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            create_dir([config.root_dir])  # create root diretory refer config.yaml

            data_ingestion_config = DataIngestionConfig(
                root_dir= config.root_dir,
                source_URL= config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
            return data_ingestion_config
        except Exception as e:
            raise SummaryException(e,sys)
        
    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            config = self.config.data_transformation

            create_dir([config.root_dir])

            data_transformation_config = DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name= config.tokenizer_name
            )
            return data_transformation_config
        except Exception as e:
            raise SummaryException(e,sys)