"""Safe built-in tools. No shell commands are executed here."""
from datetime import datetime
import ast
import operator

_ALLOWED = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod, ast.Pow: operator.pow,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
}

def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        if isinstance(node.op, ast.Pow) and abs(node.right.value) > 8:
            raise ValueError("Exponent too large")
        return _ALLOWED[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.operand))
    raise ValueError("Only basic arithmetic is allowed")

def calculate(expression: str):
    tree = ast.parse(expression, mode="eval")
    return _eval(tree.body)

def run_command(text: str):
    if text == "/time":
        return datetime.now().astimezone().strftime("%H:%M:%S %Z")
    if text == "/date":
        return datetime.now().astimezone().strftime("%A, %d %B %Y")
    if text.startswith("/calc "):
        try:
            return str(calculate(text[6:]))
        except Exception as exc:
            return f"Calculator error: {exc}"
    return None
