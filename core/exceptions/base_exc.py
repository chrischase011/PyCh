class PychException(Exception):
    """Base exception for all Pych errors."""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.__str__())

    def __str__(self):
        location = f" at Line {self.line}, Column {self.column}" if self.line is not None else ""
        return f"[Pych Error]{location}: {self.message}"
