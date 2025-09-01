# Method 1: Simple expression parser
def simple_calculator():
    """Parse simple expressions like '5 + 3' or '10 * 2'"""
    expression = input("Enter the operation (e.g., 5 + 3): ").strip()
    
    # Split the expression into parts by spaces
    parts = expression.split()
    
    if len(parts) != 3:
        return "Invalid format! Use: number operator number"
    
    try:
        a = float(parts[0])  # First number
        operator = parts[1]  # Operator
        b = float(parts[2])  # Second number
        
        # Evaluate based on operator
        if operator == '+':
            return addition(a, b)
        elif operator == '-':
            return subtraction(a, b)
        elif operator == '*':
            return multiplication(a, b)
        elif operator == '/':
            return division(a, b)
        else:
            return "Invalid operator!"
            
    except ValueError:
        return "Invalid numbers!"
    
# Define arithmetic functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Main program loop
def main():
    print("Python Calculator")
    
    while True:
        print("\nChoose a method:")
        print("1 - Simple parser")
        print("0 - Exit")
        
        choice = input("Choose (1-0): ").strip()
        
        if choice == '1':
            result = simple_calculator()
            print(f"Result: {result}")
        elif choice == '0':
            print("Exiting the calculator...")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
