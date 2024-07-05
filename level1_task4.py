def calculator():
    # Prompt user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user to enter an operator
    operator = input("Enter an operator (+, -, *, /, %): ")

    # Perform the operation based on the input
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        # Handle division by zero
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

    return f"The result of {num1} {operator} {num2} is: {result}"


# Run the calculator
print(calculator())
