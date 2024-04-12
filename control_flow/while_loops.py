# Task 3

# Task 3: While loops
# Create a new file called "while_loops.py" or similar
# Create a variable called "x", assign it the value 0
# Create a while loop that loops while x is less than 10.
# Everytime the loop completes it should:
# - Print the value of x to the screen in an f-string
# - Increment (add 1 to x)
# So the output should be:
# print x -> 0
# print x -> 1
# print x -> 2
# print x -> 3
# print x -> 4
# print x -> 5
# print x -> 6
# print x -> 7
# print x -> 8
# print x -> 9

# If commented out there will be a error
# Create a variable called "x" and assign it the value 0

x = 0

# Create a while loop that loops while x is less than 10
while x < 10:
    # Print the value of x to the screen using an f-string
    print(f"x -> {x}")

    # Increment x by 1
    x += 1
    # x = x+1

    # Check if x is greater than 4
    if x > 4:
        break  # Break out of the loop if x is greater than 4

# If you didn't increment x each time the loop completes,
# the while loop would continue indefinitely because the
# condition x < 10 would always be true. This would result
# in an infinite loop, and the program would never stop executing.
