# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hello")
# Print a list of starters
print("Nachos, Halloumi")
# Take an input for the user for their starter
starter_choice = input("Input: ")
# Print a list of mains
print("Chicken, Beef")
# Take an input for the user for their main course
main_choice = input("Input: ")
# Print a list of desserts
print("Ice cream, Cheesecake")
# Take an input for the user for their dessert
dessert_choice = input("Input: ")
# Print all of the user's choices
print(starter_choice,main_choice,dessert_choice)
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = [starter_choice, main_choice, dessert_choice ]




print(f"Your starter, {customer_order_list[0]} \n"
      f"Your main, {customer_order_list[1]} \n"
      f"Your dessert, {customer_order_list[2]} \n ")
# level 3
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
customer_order_dictonary = {"starter": "",
                    "main": "",
                    "dessert": ""}

customer_order_dictonary["starter"] = {"name": customer_order_list[0], "price": 25}
customer_order_dictonary["main"] = {"name": customer_order_list[1], "price": 500}
customer_order_dictonary["dessert"] = {"name": customer_order_list[2], "price": 2500}

print(f"Your bill is £{customer_order_dictonary["starter"]["price"] + customer_order_dictonary["main"]["price"]
+ customer_order_dictonary["dessert"]["price"]}")

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.