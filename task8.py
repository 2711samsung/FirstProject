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
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

    elif operations == 'subtract':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

    elif operations == 'multiply':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

    elif operations == 'divide':
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")

    elif operations == 'power':
            result = power(num1, num2)
            print(f"{num1} ^ {num2} = {result}")
while True:
    command = input("Choose operation (add/subtract/multiply/divide/power/quit): ")
    if command in ['add', 'subtract', 'multiply', 'divide', 'power']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a number.")
            continue

        perform_calculator(command, num1, num2)

    elif command == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid operation. Please choose a valid operation.")