# This is a simple calculator using match-case statements to perform basic arithmetic operations.
# 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ").strip()

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter +, -, *, or /.")
        
        
        # commit messages
        # feat: Implemented a simple calculator using match-case statements
        # refactor: Simplified the calculator logic and improved error handling
        # docs: Added comments to explain the calculator functionality