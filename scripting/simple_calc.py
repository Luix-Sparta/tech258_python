# Simple calculator functions

from math_operators import *


def main():
    print("Welcome to the calculator!")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operation"

    print("Result:", result)


if __name__ == "__main__":
    main()


# A package is multiple modules bundled into one.

# Library = catch all ters. Tends to be used for large packages.
