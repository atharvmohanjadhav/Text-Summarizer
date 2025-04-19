from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_trainer import ModelTraininer
from src.text_summarizer.exception.exception import SummaryException
from src.text_summarizer.logging_info import logger
import sys

class ModelTrainerPipeline:
    def __init__(self):
        pass
        
    def initiat_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTraininer(config=model_trainer_config)
            model_trainer.train()

        except Exception as e:
            raise SummaryException(e,sys)
    
