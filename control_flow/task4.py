# Task 4: Improving existing code with control flow
# 1. Loop until age is all digits
# Look at this code:
# # Ask user for their age
# age = input("What is your age? ")
#
# print(f" Your age is {age}")


# The problem with this code is that even if the user is 20,
# they could enter "20" or "twenty".
# Let's standardise the input to get the age as digits...
# Starting code - replace comments in CAPITALS with your code:

# SET VARIABLE user_prompt TO TRUE
user_prompt = True

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
age = input("What is your age? ")

# PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
if age.isdigit() is True:
    # Convert age to an integer
    age = int(age)

    # ADD IF STATEMENT HERE TO CHECK IF age IS NOT GREATER THAN 117
    if age <= 117:
        # SET user_prompt TO FALSE
        user_prompt = False
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("Please enter a valid age below 117.")
else:
    # TELL USER THE PROBLEM WITH THEIR INPUT
    print("Your age is not a digit")

# PRINT THE AGE
print(f"Your age is {age}")