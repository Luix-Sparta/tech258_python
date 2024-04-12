# Task 2: Mixed data type list

user = []

# Method one

# user input
# print("Hi, What is your name? ")
# name = input()
# user.append(name)
# print("What is your age? ")
# age = input()
# user.append(age)
# print("What is your DOB? ")
# dob = input()
# user.append(dob)

# print("Hi " + name + ". You are " + age + " and you were born on " + dob)

# Method two

# Ask for user's name, age, and DOB and append them to the list
user.append(input("Hi, What is your name? "))
user.append(int(input("What is your age? ")))
user.append(input("What is your DOB? "))


print(f"Hi {user[0]},You are {user[1]} years old and you were born on {user[2]}")
print(type(user[1]))

# Get user's height
user.append(float(input("Enter your height in centimeters: ")))
print(f"You are {user[-1]}cm")