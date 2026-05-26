def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def perform_calculator(operations, num1, num2):
    if operations == 'add':
            return add(num1, num2)

    elif operations == 'subtract':
            return subtract(num1, num2)

    elif operations == 'multiply':
            return multiply(num1, num2)

    elif operations == 'divide':
            return divide(num1, num2)

    elif operations == 'power':
            return power(num1, num2)
    
symbols = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
    "power": "**"
}

while True:
    operations = input("Choose operation (add/subtract/multiply/divide/power/quit): ")
    
    if operations in ['add', 'subtract', 'multiply', 'divide', 'power']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a number.")
            continue

        result = perform_calculator(operations, num1, num2)

        if result is None:
            print("Error: Division by zero is not allowed.")

        else:
            print(f"{num1} {symbols[operations]} {num2} = {result}")



    elif operations == 'quit':
        print("Goodbye!")
        break
    
    else:
        print("Invalid operation. Please choose a valid operation.")