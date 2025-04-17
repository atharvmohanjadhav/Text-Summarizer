from src.text_summarizer.logging_info import logger

from src.text_summarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "data ingestion stage"

try:
    logger.info("Data Ingestion started!")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiat_data_ingestion()
    logger.info("data ingestion done!")
except Exception as e:
    logger.exception(e)
    raise e