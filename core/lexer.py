import re
from core.exceptions.lexer_exc import LexerException

# Define token types using regex
TOKEN_SPECIFICATION = [
    ('T_OPEN', r'<\?::'),       # Opening tag
    ('T_CLOSE', r'::\?>'),      # Closing tag
    ('T_ECHO', r'->'),        # Echo keyword
    ('T_STRING', r'"[^"]*"'),   # String (inside double quotes)
    ('T_SEMICOLON', r';'),      # Semicolon
    ('T_IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
    ('T_LEFT_PAREN', r'\('),    # Left parenthesis
    ('T_RIGHT_PAREN', r'\)'),   # Right parenthesis
    ('T_COMMA', r','),          # Comma
    ('T_WHITESPACE', r'\s+'),   # Ignore spaces and newlines
    ('T_UNKNOWN', r'.')         # Catch-all for unknown characters
]

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, Line {self.line}, Col {self.column})"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.line = 1
        self.column = 1

    def tokenize(self):
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
        position = 0

        for match in re.finditer(token_regex, self.code):
            token_type = match.lastgroup
            token_value = match.group()
            start_pos = match.start()
            column = start_pos - position + 1

            if "\n" in token_value:
                self.line += token_value.count("\n")
                self.column = 1
            else:
                self.column += len(token_value)

            if token_type == "T_WHITESPACE":
                continue

            if token_type == "T_UNKNOWN":
                raise LexerException(f"Unknown token '{token_value}'", self.line, column)

            self.tokens.append((token_type, token_value))
            position = start_pos + len(token_value)

        return self.tokens