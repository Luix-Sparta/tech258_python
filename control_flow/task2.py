list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# 1.Under the starter code, write a loop to print double each number in the list "list_data"
for number in list_data:
    print(number * 2)

# 2.Write another loop on the next line,
#   this one should print items inside of the "embedded_lists" list.
#   The output should be:
#   [1, 2, 3]
#   [4, 5, 6]

for data in embedded_lists:
    print(data)

# 3. Create another loop inside of the "embedded_lists" for loop to list each individual item
# in each list.
# Output should be:
# [1, 2, 3]
# 1
# 2
# 3
# [4, 5, 6]
# 4
# 5
# 6

# Loop through each embedded list
for sublist in embedded_lists:
    print(sublist)  # Print the entire sublist
    # Loop through each individual item in the sublist
    for item in sublist:
        print(item)  # Print each individual item



# 4. Write a new loop on a new line.
# This one should loop through the dictionary "dict_data".
# The output should be:
# 1
# 2
# 3

for data in dict_data:
    print(data)

# 5. Write another loop, this time it should
# use the built-in dictionary method value()
# to print each value for each key inside the dictionary

for data in dict_data.values():
        print(data)

# 6. Copy and paste your last loop on a newline.
# Create an embedded loop (loop inside the loop you pasted)
# to extract and print the values within the dictionary of
# each ittem WITHIN THAT dictionary. Here is the expected output:
# Bronson
# $0.05
# Masha
# $3.66
# Roscoe
# $1.14

for data in dict_data.values():
    for value in data.values():
        print(value)

# 7. Write another loop to loop through the dictionary "dict_data",
# but this time only print out the money values.
# The output should be:
# $0.05
# $3.66
# $1.14

for data in dict_data.values():
        print(data["money"])

# 8. Write one final loop. This loop should loop through
# the items in "list_data" and include a nested (indented)
# if statement inside the loop so that each loop will check
# the number it is currently on to see if:
# - if the number is less than 3, it prints 'less than 3'
# - if the number equals 3, it prints 'I found three'
# - if the number is greater than 3, it prints 'greater than 3'
# The output should be:
# less than 3
# less than 3
# I found three
# greater than 3
# greater than 3

for data in list_data:
    if data < 3:
        print("less than 3")
    elif data == 3:
        print("I found three")
    elif data > 3:
        print("greater than 3")