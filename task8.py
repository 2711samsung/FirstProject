def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):

    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
  
    if num2 != 0:
        return num1 / num2
    else:
        print("Cannot divide by zero.")
        return None

def power(num1, num2):
    return num1 ** num2

def perform_calculator(operations, num1, num2):
    if operations == 'add':
         result = add(num1, num2)

    elif operations == 'subtract':
        result = subtract(num1, num2)

    elif operations == 'multiply':
        result = multiply(num1, num2)

    elif operations == 'divide':
        result = divide(num1, num2)

    elif operations == 'power':
            result = power(num1, num2)
    
    if isinstance(result, str): 
            print(result)
    else:
        symbol = {
            'add': '+',
            'subtract': '-',
            'multiply': '*',
            'divide': '/',
            'power': '**'}
        
        print(f"{num1} {symbol[operations]} {num2} = {result}")

while True:
    command = input("Choose operation (add/subtract/multiply/divide/power/quit): ")
    
def perform_calculator():
    if command == 'add':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

    elif command == 'subtract':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

    elif command == 'multiply':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

    elif command == 'divide':
            if num2 != 0:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            else:
                print("Cannot divide by zero.")

    elif command == 'power':
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

        result = perform_calculator(command, num1, num2)

    elif command == 'quit':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid operation. Please choose a valid operation.")


        perform_calculator()

    elif command == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid operation. Please choose a valid operation.")
