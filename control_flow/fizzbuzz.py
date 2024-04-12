# Task 5

# FizzBuzz program
for num in range(1, 101):  # Loop through numbers from 1 to 100
    if num % 3 == 0 and num % 5 == 0:  # Check if the number is a multiple of both 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0:  # Check if the number is a multiple of 3
        print("Fizz")
    elif num % 5 == 0:  # Check if the number is a multiple of 5
        print("Buzz")
    else:
        print(num)  # Print the number if it's not a multiple of 3 or 5
