import sys

class CustomException(Exception):
    def __init__(self, message : str, errors_detail : Exception = None):
        self.error_message = self.get_detailed_error_message(message, errors_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message : str, errors_detail : Exception) -> str:
        _, _, exc_tb = sys.exc_info()
        line_number = exc_tb.tb_lineno 
        file_name = exc_tb.tb_frame.f_code.co_filename
        detailed_message = f"{message} | Error : {errors_detail} | File : {file_name} | Line : {line_number}"
        return detailed_message
    
    def __str__(self):
        return self.error_message