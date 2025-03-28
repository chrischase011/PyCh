from core.functions.nodes import EchoStatement

class Interpreter:
    def run(self, ast):
        result = []
        for node in ast:
            if isinstance(node, EchoStatement):
                result.append(node.value)
        return "\n".join(result)
