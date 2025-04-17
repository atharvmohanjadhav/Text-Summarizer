from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.exception.exception import SummaryException
from src.text_summarizer.logging_info import logger
import sys

class DataIngestionPipeline:
    def __init__(self):
        pass
        
    def initiat_data_ingestion(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingesion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            data_ingestion.dowload_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise SummaryException(e,sys)