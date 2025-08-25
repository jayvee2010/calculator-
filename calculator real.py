def calculator():

    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    while True:
        try:
            # Get user input for the first number, operator, and second number
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Handle division by zero
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue  # Skip to the next iteration
                result = num1 / num2
            else:
                print("Error: Invalid operator. Please use one of +, -, *, /")
                continue  # Skip to the next iteration

            print("result:",num1, operator, num2, "=",result)

        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
            continue  # Skip to the next iteration

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

if __name__ == "__main__":
    calculator()
