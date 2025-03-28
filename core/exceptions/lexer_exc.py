from core.exceptions.base_exc import PychException

class LexerException(PychException):
    """Exception raised for lexical errors in Pych."""
    def __init__(self, message, line, column):
        super().__init__(message, line, column)
