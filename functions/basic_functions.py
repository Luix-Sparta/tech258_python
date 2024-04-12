# Functions

# DRY - Don't Repeat Yourself

# function with no arguments

def print_something():
    print("something has been printed")


print_something()


def print_something2(print_string):
    print(print_string)


print_something2("Hello")


def print_something3(name):
    print("Hello, my name is " + name)


print_something3("Hello")


# function with args

def addition(int1, int2):
    int3 = int1 + int2
    return int3


print(addition(1, 2))


# default arguments

def addition2(int1=2, int2=2):
    int3 = int1 + int2
    return int3


print(addition2(1, 2))
print(addition2(int2=2))


# multiple arguments

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)


multi_args(2, "2", 3)


# type hints
def division(denom: int, num: int) -> float:
    return denom / num


print(division(5, 3))
