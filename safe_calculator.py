# Program: Safe Calculator

# Taking input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing division
    result = num1 / num2

    # Displaying the result
    print("Result:", result)

# Handling division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling invalid input
except ValueError:
    print("Error: Please enter valid numbers.")
