# Sets and Frozen Sets

# Create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Sets are UNORDERED and UNINDEXED

# Error
# print(fruits[0])

# Add an element
fruits.add("orange")
print(fruits)

# Remove an element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate
# There can be no duplicates in a set
fruits.add("banana")
print(fruits)

# convert list to a set to remove duplicates
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)

int_set = {1, 2, 3, 4, "string"}
print(int_set)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
print(set_a - set_b)

# Frozen set --> IMMUTABLE SET

frozen_set = frozenset(["hello", "world"])
print(frozen_set)

# Error
# frozen_set.add("!")

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)