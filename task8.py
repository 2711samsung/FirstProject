def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None

def power(num1, num2):
    return num1 ** num2

def perform_calculator(command, num1, num2):
    operations = command
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

while True:
    command = input("Choose operation (add/subtract/multiply/divide/power/quit): ")
    
    if command in ['add', 'subtract', 'multiply', 'divide', 'power']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a number.")
            continue

        result = perform_calculator(command, num1, num2)
        
        if result is None:
            print("Error: Division by zero is not allowed.")
        elif command == 'add':
            print(f"{num1} + {num2} = {result}")
        elif command == 'subtract':
            print(f"{num1} - {num2} = {result}")
        elif command == 'multiply':
            print(f"{num1} * {num2} = {result}")
        elif command == 'divide':
            print(f"{num1} / {num2} = {result}")
        elif command == 'power':
            print(f"{num1} ** {num2} = {result}")

    elif command == 'quit':
        print("Goodbye!")
        break
    
    else:
        print("Invalid operation. Please choose a valid operation.")