import torch
from datasets import load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from src.text_summarizer.exception.exception import SummaryException
from src.text_summarizer.entity import ModelTrainingConfig
import os
import sys

class ModelTraininer:
    def __init__(self,config:ModelTrainingConfig):
        self.config = config

    def train(self):
        try:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
            model_peg = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
            seq2seq_data_coll = DataCollatorForSeq2Seq(tokenizer,model=model_peg)


            # load the data
            data_sam_pt = load_from_disk(self.config.data_path)
            trainer_args = TrainingArguments(
                output_dir=self.config.root_dir,
                num_train_epochs=1,  # okay for initial testing
                warmup_steps=100,  # reduce since training is short/small batch
                per_device_train_batch_size=1,  # safe for CPU
                per_device_eval_batch_size=1,   # safe for CPU
                weight_decay=0.01,
                logging_steps=10,
                eval_strategy="epoch",  # switch to epoch-based since steps=500 makes no sense with small data
                save_strategy="epoch",  # save at epoch end, not every 1e6 steps
                gradient_accumulation_steps=4,  # reduce from 16 (CPU benefits more from frequent steps)
                save_total_limit=1,  # keep only the latest checkpoint
                fp16=False,  # disable mixed precision — no GPU
                dataloader_num_workers=0,  # safe for CPU (0 or 1)
                remove_unused_columns=True,  # slightly faster
                disable_tqdm=False  # keep progress bars
            )
            trainer = Trainer(model=model_peg,args=trainer_args,
                    tokenizer=tokenizer,data_collator=seq2seq_data_coll,
                    train_dataset=data_sam_pt["test"],
                    eval_dataset=data_sam_pt["validation"])
            # trainer.train()

            model_peg.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsung-model"))
            tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
        except Exception as e:
            raise SummaryException(e,sys)
