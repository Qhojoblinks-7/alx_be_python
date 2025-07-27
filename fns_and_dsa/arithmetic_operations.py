def perform_operation(num1, num2, operation):
    """
    Performs an arithmetic operation on two numbers.

    :param num1: First number (float or int)
    :param num2: Second number (float or int)
    :param operation: Type of operation ('add', 'subtract', 'multiply', 'divide')
    :return: Result or error message (str or float)
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation type. Choose 'add', 'subtract', 'multiply', or 'divide'."
