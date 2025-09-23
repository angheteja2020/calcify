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

def divide(n1, n2):
    """Divides two numbers, with a built-in safety check."""
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

def power(n1, n2):
    """Calculates n1 to the power of n2."""
    return n1 ** n2

def sqrt(n1):
    """Calculates the square root of a number."""
    if n1 < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(n1)

def run_calculator():
    """The main function to runu the calculator loop."""
    print("Welcome to Calcify!")
    print("Enter calculations like '5 + 3', or type 'quit' to exit.")

    # A dictionary mapping symbols to our functions
    operations = {
        '+': add,
        '-': substract,
        '*': multiply,
        '/': divide,
        '^': power,
    }

    # One-number operations
    unary_operations = {
        'sqrt': sqrt,
    }

    while True:
        user_input = input(">>> ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        parts = user_input.split()

        try:
            # Check for unary operations first (e.g., "sqrt 16")
            if len(parts) == 2 and parts[0].lower() in unary_operations:
                op = parts[0].lower()
                n1 = float(parts[1])
                calculation_function = unary_operations[op]
                result = calculation_function(n1)
                print(result)

            # Check for binary operations (e.g., "5 + 3")
            elif len(parts) == 3:
                n1 = float(parts[0])
                op = parts[1]
                n2 = float(parts[2])

                if op in operations:
                    calculation_function = operations[op]
                    result = calculation_function(n1, n2)
                    print(result)
                else:
                    print(f"'{op}' is not a valid operator.")
            else:
                raise ValueError("Invalid format")

        except (ValueError, IndexError):
            # This is our "catch-all" for bad input
            print("Invalid format. Please enter in the format: number operator number (e.g., 5 * 3)")

if __name__ == "__main__":
    run_calculator()