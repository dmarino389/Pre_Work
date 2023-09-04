# Line 1-20: Different data types in Python

# This is a single-line comment. Everything on the same line as the hashtag will be considered part of the comment.

x = 10  # variable x has a value of 10

name = "Kevin"  # this is a string, strings are used to represent text data. I can enclose them in single or double quotes

age = 25  # this is an integer (int). Integers represent whole numbers without any decimal places. They can be positive or negative. These are essential for numerical computations in Python

pi = 3.14  # these are floats (float). Floats are used to represent decimal numbers in Python. They are written with a decimal point. They enable precise calculation for scientific analysis, financial modeling, or anything that needs to be specific.

numbers = [1, 2, 3, 4, 5]  # Lists (list). Lists are ordered collections of items enclosed in square brackets []. They can contain elements of different types, and the elements can be modified. Lists are mutable, meaning you can change, add, or remove elements.

person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
# Above is a dictionary in Python or (dict). Dictionaries in Python store and retrieve values using unique keys. Key-Value Mapping: Create a mapping between keys and their associated values. Ordered Collection: Starting from Python 3.7, dictionaries are now ordered, preserving the order of key-value pairs.

# ... (other comments)

# Math operations in Python. Lines 24-45

result = 2 + 3  # This is the addition operator in Python using a + symbol
print(result)  # output: 5

result = 5 - 2  # This is the subtraction operator in Python
print(result)  # output: 3

# ... (other operations)

# Flow statements in Python. (51-89)

# ... (comments about if, elif, else statements)

# ... (comments about loops)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:  # if I used for fruits in fruits then that would be variable shadowing and that would cause confusion
    print(fruit)
    # output: apple, banana, orange

# ... (other comments)

# Built-in Functions: Range

# ... (comment about the range function)

range_values = range(1, 10, 2)  # returns a sequence of odd numbers from 1 to 9
print(list(range_values))  # output: [1, 3, 5, 7, 9]

# ... (other comments)

# Data Type Conversion

# ... (comments about type conversion)

num_str = "42"

# Convert string to integer
num_int = int(num_str)
print(num_int)  # Output: 42
print(type(num_int))  # Output: <class 'int'>

# Convert string to float
num_float = float(num_str)
print(num_float)  # Output: 42.0
print(type(num_float))  # Output: <class 'float'>

# ... (other comments)

# Integer/Float to String Conversion

# ... (To convert an ineger or float to a string, you can use the str() function)

num_str_int = str(num_int)
print(num_str_int)  # output will be "42"
print(type(num_str_int))  # Output: <class 'str'>

num_str_float = str(num_float)
print(num_str_float)  # output will be "42.0"
print(type(num_str_float))  # Output: <class 'str'>

# Integer/Float to String Formatting

#...(if you need more control over the formatting of the resulting string, you can use the format()method or f-strings(formatted string literals). In the example below, "{:.2f}" represents theformat string that formats the float with two decimal places.

num_float = 3.14

formatted_str = "{:.2f}".format(num_float)
print(formatted_str) # This is the formatting method and the output will be "3.14"

formatted_str = f"{num_float:.2f}"
print(formatted_str) # This is the f-string method and the output will be "3.14"

#------------------

# Logical & Procedural

#-------------------

#Logical Thinking

#...(logical thinking involves breaking down a problem into smaller logical steps and then solving it using a series of conditional statemtns and logical operations. In Python, logical thinking is often implemented using control structures like conditionals (if-else statements) and loops)

num = int(input("Enter a number: ")) #this is to check whether the number is positive or negative

if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")

# Procedural Thinking

#...(Procedural thinking involves breaking down a problem into a series of ordered steps or specific task or operation. in Python, procedural thinking is often implemented using functions, which allow you to encapsulate a set of instructions that can be refused)

def factorial(n): # This is to calculate the factorial of a number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
fact = factorial(num)
print(f"the factorial of {num} is {fact}.")