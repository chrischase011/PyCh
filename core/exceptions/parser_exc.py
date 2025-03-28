from core.exceptions.base_exc import PychException

class ParserException(PychException):
    """Exception raised for parsing errors in Pych."""
    def __init__(self, message, position):
        super().__init__(message)
        self.position = position