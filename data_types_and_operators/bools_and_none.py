# Bools and None

# Booleans can be: True or False

a = True
b = False

# print(a == b)  # False
# print(a != b)  # True
#
# # False is ALWAYS 0
# print(a >= b) # True
# print(a <= b) # False

# Booleans methods

# We can use these to make decisions
hi = "Hello World"
# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.isupper()) # False
# print(hi.endswith("d")) # True
# print(hi.startswith("H")) # True

# What happens when you try to convert a string to a bool (using casting)?

# # Always True unless the string is empty
# print(bool(hi)) # True
# print(bool("")) # False
#
# # What happens when e convert a number to a bool?
# print(bool(0)) # False - Only 0 is over False
# print(bool(40)) # True
# print(bool(-23)) # True

# The value of None

# None is an object, it is essentially a placeholder

# None when converted to a bool is False
print(bool(None))

# None != False

x = None

print(x == False) # False
print(x == None) # True

print(type(x))

# None is best used over an empty string etc. It is less likely to cause problems down the line.
