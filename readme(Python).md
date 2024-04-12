# Tech 258 - Python

## Introduction

Welcome to the Tech 258 - Python repository! In this document, we'll cover various aspects of Python programming language.

## What is Python? 

Python is a versatile and beginner-friendly programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.

## History of Python

Python's development started in the late 1980s and the first version, Python 0.9.0, was released in 1991. Guido van Rossum, the creator of Python, aimed to create a language that was easy to read, write, and understand.

## Why Python is Popular

- **Simplicity:** Python's clean and easy-to-read syntax makes it ideal for beginners and experienced programmers alike.
- **Versatility:** Python can be used for web development, data analysis, machine learning, artificial intelligence, scientific computing, automation, and more.
- **Extensive Libraries:** Python has a rich ecosystem of libraries and frameworks that facilitate various tasks without reinventing the wheel.
- **Community Support:** Python has a large and active community of developers who contribute to its growth and development.

## Python for DevOps Engineers

Python is particularly popular among DevOps engineers due to:
- **Automation:** Python's simplicity and extensive libraries make it well-suited for automating infrastructure management tasks.
- **Versatility:** Python can be used to create scripts, tools, and utilities for various DevOps activities such as configuration management, deployment automation, monitoring, and logging.

## Virtual Environment (venv)

A virtual environment is a self-contained directory that contains a Python interpreter and a set of libraries specific to a particular project. It allows you to isolate dependencies and avoid conflicts between different projects.

## pip Package Manager

pip is the package installer for Python. It is used to install, uninstall, and manage Python packages from the Python Package Index (PyPI) or other package repositories.

## Scripting vs Programming

- **Scripting:** Scripting involves writing scripts, which are typically short programs or sequences of commands written in a scripting language like Python. Scripts are often used for automation, system administration, and rapid prototyping.
- **Programming:** Programming involves writing larger, more complex applications or software systems using traditional programming languages like Python, Java, or C++.

## Base Python Libraries

Python comes with a standard library that provides a wide range of modules and packages for various tasks such as file I/O, networking, data manipulation, and more.

Some of the base Python libraries include:
- `os`
- `sys`
- `datetime`
- `math`
- `random`
- `re`
- `json`
- `csv`
- `socket`

## Popular External Libraries

In addition to the base Python libraries, there are numerous external libraries that extend Python's functionality for specific domains or tasks.

Some of the most popular external libraries include:
- `NumPy`
- `pandas`
- `Matplotlib`
- `Flask`
- `Django`
- `TensorFlow`
- `PyTorch`
- `SQLAlchemy`
- `Requests`
- `BeautifulSoup`
- `Scrapy`

## Python Tasks

### Code Examples

#### Task 1: BMI Program

```python
# Get user's height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print BMI
print("Your BMI is:", round(bmi, 2))
```
#### Task 2: Tip Calculator
```python
# Get the bill amount
bill_amount = float(input("Enter the bill amount: $"))

# Calculate the tip
tip_percentage = float(input("Enter the tip percentage (10-15%): "))
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate total bill with tip
total_bill = bill_amount + tip_amount

# Ask for the number of people to split with
num_people = int(input("Enter the number of people to split with: "))

# Calculate the split bill per person
split_bill = total_bill / num_people

# Print the split bill per person, rounded to 2 decimal places
print("Each person should pay: £", round(split_bill, 2))
```

## Conclusion

Python is a powerful and versatile programming language with a rich ecosystem of libraries and tools. Whether you're a beginner or an experienced developer, Python offers a wide range of capabilities for various domains and applications.

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

---