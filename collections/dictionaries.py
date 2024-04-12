# Dictionaries

# key = value pairs
# key is the reference, value is the data storage mechanism you want (int, string etc.)

student1 = {
    "name": "Susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up", "collections"]
}

print(student1)
print(student1["name"])
print(student1["completed_lesson_names"][0])

student1["completed_lessons"] = 3
print(student1["completed_lessons"])
student1["completed_lesson_names"].pop()
print(student1["completed_lesson_names"])

# getting the keys for a dictionary
print(type(student1.keys()))