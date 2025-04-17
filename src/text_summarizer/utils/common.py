import os
from box.exceptions import BoxValueError
import yaml
from src.text_summarizer.logging_info import logger
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from src.text_summarizer.exception.exception import SummaryException
import sys

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    try:
        with open(path_to_yaml,"rb") as file:
            cont = yaml.safe_load(file)
            logger.info(f"yaml file {path_to_yaml} loaded succesfully!")
            return ConfigBox(cont)
    except BoxValueError:
        raise ValueError("yaml file is empty!")
    except Exception as e:
        raise SummaryException(e,sys)
    
@ensure_annotations
def create_dir(path_to_dir: list, verbose=True):
    try:
        for path in path_to_dir:
            os.makedirs(path ,exist_ok= True)
            if verbose:
                logger.info(f"created dir at {path}")
    except Exception as e:
        raise SummaryException(e,sys)
    