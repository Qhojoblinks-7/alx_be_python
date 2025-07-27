
def perform_operation(num1, num2, operation):
    """
    This function performs a simple arithmetic operation.
    It performs operation on two numbers and returns the result based on the operation type chosen.
    It prompts the user to enter two numbers and an operation type (addition, subtraction, multiplication, or division).
    
    the operation parameter accepts a string that indicates the operation type:
    - add 
    - subtract
    - divide
    - mulytiply
    
    
    The function then performs the chosen operation and returns the result using switch-case logic.
    If the user enters an invalid operation type, it returns an error message.
    :return: Result of the arithmetic operation or an error message if the operation type is invalid.
    
    """
    
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        case _:
            return "Error: Invalid operation type. Please choose 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division."

            '''
                       '''