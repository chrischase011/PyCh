from core.functions.nodes import EchoStatement
from core.exceptions.parser_exc import ParserException

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        """Returns the current token without consuming it."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def consume(self, expected_type):
        """Consumes the current token if it matches the expected type."""
        token = self.peek()
        expected_value = ""
        if token and token[0] == expected_type:
            self.position += 1
            return token
        
        
        expected_token_value = token[1] if token and token[0] == expected_type else None
        
        raise ParserException(
            f"Expected {token[0]}, got {token[1]}",
            self.position
        )

    def parse_echo(self):
        """Parses an echo statement."""
        self.consume("T_ECHO")
        string_token = self.consume("T_STRING")
        self.consume("T_SEMICOLON")
        return EchoStatement(value=string_token[1].strip('"'))

    def parse(self):
        """Parses the entire token list."""
        ast = []
        
        self.consume("T_OPEN")  # Ensure it starts with <?::
        while self.peek() and self.peek()[0] != "T_CLOSE":
            token = self.peek()
            if token[0] == "T_ECHO":
                ast.append(self.parse_echo())
            else:
                raise ParserException(f"Unexpected token {token}", self.position)

        self.consume("T_CLOSE")  # Ensure it ends with ::?>
        return ast
