


## Code

Code Snippet `this is code`

Code block 
```python
# Code line 1

# This is still code

# Code line 2
```

# Tech 258 - Python

## What is Python? What is the history of Python?

Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability and simplicity, making it suitable for beginners and experienced programmers alike.

## Why is Python popular? Why is it particularly popular for DevOps engineers?

Python's popularity stems from its simplicity, versatility, and extensive library support. It is widely used in various domains such as web development, data analysis, artificial intelligence, scientific computing, and automation. For DevOps engineers, Python's ease of use, rich ecosystem of libraries (such as Ansible, Fabric, and SaltStack), and strong community support make it an ideal choice for automating infrastructure management tasks.

## What is a virtual environment or venv?

A virtual environment (often abbreviated as venv) is a self-contained directory that contains a Python interpreter and a set of libraries specific to a particular project. It allows you to isolate dependencies and avoid conflicts between different projects by maintaining separate environments for each project.

## What is "pip"?

pip is the package installer for Python. It is used to install, uninstall, and manage Python packages from the Python Package Index (PyPI) or other package repositories. pip simplifies the process of installing third-party libraries and dependencies for Python projects.

## What is scripting? How is it different from programming?

Scripting refers to the process of writing scripts, which are typically short programs or sequences of commands written in a scripting language. Scripting languages like Python are often used for tasks such as automation, system administration, and rapid prototyping. Unlike traditional programming languages, scripting languages are interpreted rather than compiled, allowing for quick development and execution of code without the need for compilation.

## What are the base Python libraries?

Python comes with a standard library that provides a wide range of modules and packages for various tasks such as file I/O, networking, data manipulation, mathematical operations, and more. Some of the base Python libraries include `os`, `sys`, `datetime`, `math`, `random`, `re`, `json`, `csv`, and `socket`.

## What are some of the most popular external libraries?

In addition to the base Python libraries, there are numerous external libraries (also known as third-party libraries or packages) that extend Python's functionality for specific domains or tasks. Some of the most popular external libraries include:
- NumPy and pandas for data manipulation and analysis
- Matplotlib and seaborn for data visualization
- Flask and Django for web development
- TensorFlow and PyTorch for machine learning and artificial intelligence
- SQLAlchemy for database interaction
- Requests for HTTP requests
- BeautifulSoup and Scrapy for web scraping

## Optional - Try out the Python tasks I have set up here()

Feel free to explore the provided Python tasks and experiment with the code.

Please do not use git yet, we will introduce that in future lessons.

Change for demo

## Control Flow

### Task 1 - IF

#### Possible Film Ratings

The possible film ratings are "universal", "pg", "12", "12a", "15", and "18".

```python
# Set the film rating
film_rating = "12a"

# Use an if statement to check for "universal" rating
if film_rating == "universal":
    print("All age groups can watch this film")

# Check if film rating is "pg"
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")

# Check if film rating is "12" or "12a"
elif film_rating == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

# Check if film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")

# Check if film rating is "18"
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")

# Else statement for invalid ratings
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
```
Explanation:
- film_rating = "12a": Assigns the film rating to a variable.

- Use an if statement to check for "universal" rating: Comment indicating the purpose of the following if statement.

- if film_rating == "universal":: Checks if the film rating is "universal". If true, it prints a message indicating that all age groups can watch the film.

- elif film_rating == "pg":: Checks if the film rating is "pg". If true, it prints a message indicating general viewing with some scenes unsuitable for young children.

- elif film_rating == "12" or film_rating == "12a":: Checks if the film rating is "12" or "12a". If true, it prints a message explaining the classification and restrictions for children under 12.

- elif film_rating == "15":: Checks if the film rating is "15". If true, it prints a message indicating the age restriction for viewing the film.

- elif film_rating == "18":: Checks if the film rating is "18". If true, it prints a message indicating the age restriction for viewing the film.

- else:: This is the default case if none of the above conditions are met. It prints a message indicating that the provided rating is not correct and provides instructions for valid ratings.

## Task 2 - Loops in Python

## What are loops?

Loops in programming are structures that allow you to execute a block of code repeatedly. They are used to automate repetitive tasks and iterate over collections of data.

## Different types of loops:

There are mainly two types of loops in Python:
1. **For loop**: Used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object.
2. **While loop**: Executes a block of code as long as a specified condition is true.

## What can we do with loops?

Loops are used to perform repetitive tasks, such as iterating over elements in a list, processing items in a dictionary, or executing a block of code until a certain condition is met.

### What is a For loop?

A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. Here's an example:

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### What is a While loop?

A while loop executes a block of code as long as a specified condition is true. It's useful when you don't know beforehand how many times you need to iterate. Here's an example:

```python
# Use a while loop to print numbers from 1 to 5
num = 1
while num <= 5:
    print(num)
    num += 1
```

### Why use a While loop instead of a For loop?

While loops are useful when you don't know the number of iterations beforehand, or when you want to iterate until a specific condition is met.

## Dangers and Best Practices

While loops can potentially lead to infinite loops if the condition never becomes false. It's important to ensure that the condition eventually becomes false to prevent the program from running indefinitely. Additionally, it's essential to initialize loop control variables properly and update them correctly within the loop to avoid unexpected behavior.

It's a best practice to use loops judiciously and ensure that they are well-structured and efficient to avoid performance issues.

