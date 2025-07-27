from calculator import add, subtract, multiply, divide

def main():
    print("Welcome to the Simple Calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ").strip()

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        return

    print(f"The result is: {result}")
if __name__ == "__main__":
    main()