
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_eval import ModelEval
import sys
from src.text_summarizer.exception.exception import SummaryException

class ModelEvalPipeline:
    def __init__(self) -> None:
        pass

    def initiate_model_eval(self):
        try:
            config = ConfigurationManager()
            model_eval_config = config.get_model_eval_config()
            model_eval = ModelEval(config=model_eval_config)
            model_eval.eval()
        except Exception as e:
            raise SummaryException(e,sys)