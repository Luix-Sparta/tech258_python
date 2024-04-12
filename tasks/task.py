# Task 1: BMI calculator

print(f"{'*' * 27}Task 1{'*' * 27}")
print("")
print(f"{'=' * 60}")
print(f"{'*' * 23}BMI calculator{'*' * 23}")
print(f"{'=' * 60}")
print("")

# Get user's height and weight
height_cm = float(input("Enter your height in centimeters: "))  # Prompt user for height in centimeters
weight_kg = float(input("Enter your weight in kilograms: "))

# Convert height from centimeters to meters
height_m = height_cm / 100  # Convert centimeters to meters

# Calculate BMI
bmi = weight_kg / (height_m ** 2)  # Use height in meters for calculation

# Print BMI
print("Your BMI is:", round(bmi, 2))


# Task 2: Tip Calculator

print(f"{'*' * 27}Task 2{'*' * 27}")
print("")
print(f"{'=' * 60}")
print(f"{'*' * 23}Tip Calculator{'*' * 23}")
print(f"{'=' * 60}")
print("")


# Get the bill amount
bill_amount = float(input("Enter the bill amount: £"))

# Calculate the tip
tip_percentage = float(input("Enter the tip percentage(10-15%): "))
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate total bill with tip
total_bill = bill_amount + tip_amount

# Ask for the number of people to split with
num_people = int(input("Enter the number of people to split with: "))

# Calculate the split bill per person
split_bill = total_bill / num_people

# Print the split bill per person, rounded to 2 decimal places
print("Each person should pay: £", round(split_bill, 2))
