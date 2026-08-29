# Day 3 — Python Functions for RAG Implementation
# ================================================
# Topics:
# - Functions
# - Parameters
# - Arguments
# - Return values
# - Default arguments
# - Keyword arguments
# - *args
# - **kwargs
# - Lambda
# - List comprehensions
# - Dictionary comprehensions

# -------------------------
# 1. BASIC FUNCTION
# -------------------------

def say_hello():
    print("Hello")


say_hello()


# -------------------------
# 2. PARAMETERS & ARGUMENTS
# -------------------------

def greet(name):
    print("Hello", name)


# "name" is the parameter.
# "Sudais" is the argument.
greet("Sudais")


# Multiple parameters
def introduce(name, age):
    print(name)
    print(age)


introduce("Sudais", 20)


# -------------------------
# 3. RETURN
# -------------------------

def add(a, b):
    return a + b


result = add(5, 3)
print(result)


# Return ends the function.
def test():
    return 10
    # This code will not run:
    # print("Hello")


# Returning multiple values
def get_document_info():
    return "policy.pdf", 5


source, page = get_document_info()

print(source)
print(page)


# -------------------------
# 4. DEFAULT ARGUMENTS
# -------------------------

def greet_user(name="User"):
    print("Hello", name)


greet_user("Sudais")
greet_user()


# RAG-style example
def chunk_text(text, chunk_size=500):
    print("Chunk size:", chunk_size)
    return text


chunk_text("Some document text")
chunk_text("Some document text", 1000)


# -------------------------
# 5. KEYWORD ARGUMENTS
# -------------------------

def create_chunk(text, source, page):
    print(text)
    print(source)
    print(page)


# Positional arguments
create_chunk("Hello", "policy.pdf", 5)

# Keyword arguments
create_chunk(
    text="Hello",
    source="policy.pdf",
    page=5
)

# Keyword arguments can be supplied in a different order.
create_chunk(
    page=5,
    source="policy.pdf",
    text="Hello"
)


# -------------------------
# 6. *args
# -------------------------
# *args collects any number of positional arguments
# into a tuple.

def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


print(add_numbers(1, 2))
print(add_numbers(1, 2, 3, 4, 5))


# -------------------------
# 7. **kwargs
# -------------------------
# **kwargs collects any number of keyword arguments
# into a dictionary.

def create_document(**kwargs):
    print(kwargs)


create_document(
    source="policy.pdf",
    page=5,
    category="medical"
)


# Important:
# *args   -> tuple
# **kwargs -> dictionary


# -------------------------
# 8. *args + **kwargs TOGETHER
# -------------------------

def test_arguments(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


test_arguments(
    10,
    20,
    30,
    40,
    name="Sudais",
    city="Islamabad"
)


# -------------------------
# 9. LAMBDA
# -------------------------
# Lambda is a short, one-expression function.

def square(x):
    return x * x


print(square(5))

# Same basic idea with lambda
square_lambda = lambda x: x * x

print(square_lambda(5))

# Multiple parameters
multiply = lambda a, b: a * b

print(multiply(5, 4))


# -------------------------
# 10. LAMBDA WITH sorted()
# -------------------------
# Useful for sorting RAG retrieval results by score.

results = [
    {"text": "Chunk A", "score": 0.5},
    {"text": "Chunk B", "score": 0.9},
    {"text": "Chunk C", "score": 0.7}
]

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print(results)


# -------------------------
# 11. LIST COMPREHENSION
# -------------------------

numbers = [1, 2, 3, 4, 5]

squares = [
    number * number
    for number in numbers
]

print(squares)


# List comprehension with condition
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# -------------------------
# 15. PRACTICE EXERCISES
# -------------------------

# Exercise 1:
# Create a function multiply(a, b) that returns the result.

# Exercise 2:
# Create a function greet(name="User") and test it
# with and without an argument.

# Exercise 3:
# From the chunks list above, create a list containing
# only the text values.

# Exercise 4:
# Create calculate(*args) that returns the sum of all
# numbers passed to it.


# -------------------------
# Day 3 Key Reminder
# -------------------------
# Function:
# def function_name(parameters):
#     return result
#
# Keyword argument:
# name="Sudais"
#
# *args:
# many positional arguments -> tuple
#
# **kwargs:
# many keyword arguments -> dictionary
#
# Lambda:
# small one-expression function
#
# List comprehension:
# [expression for item in collection]
#
# Dictionary comprehension:
# {key: value for item in collection}
#
# Most important for RAG:
# functions + return + parameters +
# list/dictionary comprehensions
