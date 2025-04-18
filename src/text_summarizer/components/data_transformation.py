# from src.text_summarizer.config.configuration import DataTransformationConfig
from src.text_summarizer.exception.exception import SummaryException
from src.text_summarizer.entity import DataTransformationConfig
import sys
import os
from src.text_summarizer.logging_info import logger
from transformers import AutoTokenizer
from datasets import load_from_disk

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name) 
    
    def convert_to_features(self,example_batch):
        try:
            input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

            return {
                'input_ids' : input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        except Exception as e:
            raise SummaryException(e,sys)
        
    def convert(self):
        try:
            data_sam = load_from_disk(self.config.data_path)
            data_sam_pt = data_sam.map(self.convert_to_features, batched = True)
            data_sam_pt.save_to_disk(os.path.join(self.config.root_dir,"samsung_dataset"))
        except Exception as e:
            raise SummaryException(e,sys)
        
