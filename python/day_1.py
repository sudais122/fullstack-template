# Day 1 — Python Basics for RAG Implementation
# ============================================
# Topics:
# - Variables and data types
# - Strings and multiline strings
# - None
# - Operators
# - if / elif / else

# -------------------------
# 1. Variables & Data Types
# -------------------------

name = "Sudais"          # str
age = 20                 # int
score = 0.95             # float
is_student = True       # bool
address = None           # NoneType

print(name)
print(age)
print(score)
print(is_student)
print(address)

# Check the type
print(type(name))
print(type(age))
print(type(score))
print(type(is_student))
print(type(address))


# -------------------------
# 2. Strings
# -------------------------

text = "Hello, Python!"
print(text)

# Indexing
print(text[0])
print(text[-1])

# Slicing
print(text[0:5])
print(text[:5])
print(text[6:])

# Useful string methods
print(text.lower())
print(text.upper())
print(text.strip())

# f-string
source = "policy.pdf"
page = 5
message = f"Source: {source}, Page: {page}"
print(message)


# -------------------------
# 3. Multiline Strings
# -------------------------

document_text = """
Patients can cancel appointments
24 hours before the appointment.
"""

print(document_text)


# -------------------------
# 4. None
# -------------------------

author = None

if author is None:
    print("Author is not available")

# Prefer "is None" for checking None.
# None means "no value" / "value is absent".


# -------------------------
# 5. Operators
# -------------------------

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor division

# Comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators
print(a > 5 and b < 5)
print(a > 20 or b < 5)
print(not (a > 5))


# -------------------------
# 6. Assignment Operators
# -------------------------

x = 10

x += 3
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

# Bitwise assignment operators
x = 8

x &= 3       # x = x & 3
x |= 3       # x = x | 3
x ^= 3       # x = x ^ 3
x >>= 1      # x = x >> 1
x <<= 1      # x = x << 1

print(x)

# Walrus operator :=
print(y := 3)


# -------------------------
# 7. if / elif / else
# -------------------------

age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# RAG-style example
clinic_status = "open"

if clinic_status == "open":
    print("The clinic is open.")
elif clinic_status == "closed":
    print("The clinic is closed.")
else:
    print("Unknown clinic status.")


# -------------------------
# Day 1 Key Reminder
# -------------------------
# Python basics needed for RAG:
# variables, data types, strings, None,
# operators, and conditions.
