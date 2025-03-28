import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.lexer import Lexer
from core.parser import Parser
from core.interpreter import Interpreter

def run_pych_code(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    result = interpreter.run(ast)

    return result

def repl():
    print("Pych REPL - Type Pych code (type 'exit' to quit)")
    while True:
        try:
            code = input("pych> ")
            if code.strip().lower() == "exit":
                break

            output = run_pych_code(f"<?:: {code} ::?>")
            if output is not None:
                print(output)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
