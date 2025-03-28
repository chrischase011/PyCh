from core.lexer import Lexer
from core.parser import Parser

code = '<?:: echo "Hello, world!"; ::?>'
lexer = Lexer(code)
tokens = lexer.tokenize()

print("Tokens:", tokens)  # Debugging

parser = Parser(tokens)
ast = parser.parse()

print("AST:", ast)  # Should print: [EchoStatement(value='Hello, world!')]
