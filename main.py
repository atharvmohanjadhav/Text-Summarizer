from src.text_summarizer.logging_info import logger
from src.text_summarizer.exception.exception import SummaryException
import sys
from src.text_summarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionPipeline 
from src.text_summarizer.pipeline.stage2_data_transformation_pipeline import DataTransformationPipeline
from src.text_summarizer.pipeline.stage3_model_trainier_pipeline import ModelTrainerPipeline

STAGE_NAME = "data ingestion stage"

try:
    logger.info("Data Ingestion started!")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiat_data_ingestion()
    logger.info("data ingestion done!\n")
except Exception as e:
    raise SummaryException(e,sys)


try:
    logger.info("Data Transformation started!")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiat_data_transformation()
    logger.info("Data transformation done!\n") 
except Exception as e:
    raise SummaryException(e,sys)

try:
    logger.info("Model Training Start!")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiat_model_trainer()
    logger.info("Model Training Done!")
except Exception as e:
    raise SummaryException(e,sys)