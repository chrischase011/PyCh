class Node:
    """Base class for all AST nodes."""
    pass

class EchoStatement(Node):
    """Represents an echo statement in the language."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"EchoStatement(value={self.value})"
