# Task 1: Working with a list

# Collections are a way to store multiple pieces of data in one reference/object
# Lists are the most common/simplest collection

# Lists are often known as arrays in other languages

# 1. Create a list called 'shopping_list'
shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']

# 2. Print the list to the screen
print(shopping_list)

# 3. Print the data type of 'shopping_list'
print(type(shopping_list))

# 4. Print the first item in the list
print(shopping_list[0])

# 5. Print the last item in the list
print(shopping_list[-1])

# 6. Change the second item in the list to 'rice'
shopping_list[1] = 'rice'
print(shopping_list[1])

# 7. Add the item 'carrots' to the list
shopping_list.append('carrots')
print(shopping_list)

# 8. Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list
shopping_list.extend(['toffee', 'coffee'])
print(shopping_list)

# 10. Remove "bananas" from 'shopping_list'
shopping_list.remove('bananas')
print(shopping_list)

# 11. Remove the last item ('coffee') from 'shopping_list' using the pop method
shopping_list.pop()
print(shopping_list)

# 12. Use the "append" method to add an item to your list
shopping_list.append('apple')
print(shopping_list)

# 13. Use the "remove" method to remove an item from your list
shopping_list.remove('biscuits')
print(shopping_list)

# 14. Remove the last item from the list without referencing it
del shopping_list[-1]
print(shopping_list)



