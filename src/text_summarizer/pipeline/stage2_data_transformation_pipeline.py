from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_transformation import DataTransformation
from src.text_summarizer.exception.exception import SummaryException
from src.text_summarizer.logging_info import logger
import sys

class DataTransformationPipeline:
    def __init__(self):
        pass
        
    def initiat_data_transformation(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()

        except Exception as e:
            raise SummaryException(e,sys)
    
