import math

def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

def substract(n1, n2):
    """Subtracts two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Subtracts two numbers."""
    return n1 * n2

def devide(n1, n2):
    """Divides two numbers, with a built-in safety check."""
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2