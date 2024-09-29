def perform_operation(num1,num2,operation):
    """
    Perform an arithmetic operation on two numbers.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ("add", "subtract", "multiply", "divide").

    Returns:
    float: The result of the arithmetic operation.

    Raises:
    ValueError: If the operation is not one of the supported operations.
    """
    supported_operations = ["add", "subtract", "multiply", "divide"]
    if operation not in supported_operations:
        raise ValueError(f"Unsupported operation: {operation}")

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2