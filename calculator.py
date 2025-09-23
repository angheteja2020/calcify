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
    print("---" * 10)
    print("Basic Ops:   5 + 3 | 10 * 2 | 8 ^ 2")
    print("Advanced Ops:  sqrt 16")
    print("Memory Ops:  MS (Store) | MR (Recall) | MC (Clear) | M+ (Add)")
    print("Enter 'quit' to exit.")
    print("---" * 10)

    memory = 0.0
    last_result = 0.0

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
        user_input = input(">>> ").lower()

        if user_input == 'quit':
            print("Goodbye!")
            break

        # --- MEMORY COMMANDS ---
        if user_input == 'mc':
            memory = 0.0
            print("Memory cleared.")
            continue 

        if user_input == 'ms':
            memory = last_result
            print(f"Stored {last_result} to memory.")
            continue

        if user_input == 'm+':
            memory += last_result
            print(f"Added {last_result} to memory. New value: {memory}")
            continue

        # --- PARSING AND CALCULATION ---
        # The MR (Memory Recall) logic is handle here
        # It replaces 'mr' with the actual number from memory
        if 'mr' in user_input:
            user_input = user_input.replace('mr', str(memory))
            print(f"Input: {user_input}")

        parts = user_input.split()

        try:
            # Check for unary operations first (e.g., "sqrt 16")
            if len(parts) == 2 and parts[0] in unary_operations:
                op = parts[0]
                n1 = float(parts[1])
                result = unary_operations[op](n1)

            # Check for binary operations (e.g., "5 + 3")
            elif len(parts) == 3:
                n1 = float(parts[0])
                op = parts[1]
                n2 = float(parts[2])
                result = operations[op](n1, n2)
            else:
                raise ValueError("Invalid format")
            
            # --- UPDATE AND DISPLAY RESULT ---
            if isinstance(result, str): # Check if the result is an error message
                print(result)
            else:
                print(result)
                last_result = result # IMPORTANT: Update last_result on success

        except (ValueError, IndexError):
            # This is our "catch-all" for bad input
            print("Invalid format or command. Please try again.")

if __name__ == "__main__":
    run_calculator()