import os
import sys

class SummaryException(Exception):
    def __init__(self, error_msg,error_details: sys):
        self.error_msg = error_msg
        _,_,detail = error_details.exc_info()

        self.file_name = detail.tb_frame.f_code.co_filename
        self.line_no = detail.tb_lineno

    def __str__(self):
        return f"The error occured in file: {self.file_name} in line number [{self.line_no}] error message is [{self.error_msg}]"
        

    