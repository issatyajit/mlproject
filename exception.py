import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message: str):
        _, _, exc_tb = sys.exc_info()
        if exc_tb is not None:
            fname = exc_tb.tb_frame.f_code.co_filename
            line_no = exc_tb.tb_lineno
        else:
            fname = "Unknown"
            line_no = "Unknown"
        super().__init__(error_message)
        self.error_message = error_message
        self.file_name = fname
        self.line_number = line_no

    def __str__(self):
        return f"Error in file '{self.file_name}', line {self.line_number}: {self.error_message}"