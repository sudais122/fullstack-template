
from pathlib import Path
import math

from mymath import add, divide, multiply, subtact
import text_utils


# =========================================================
# 1. CUSTOM MODULE PRACTICE
# =========================================================

# print(add(12, 3))
# print(divide(18, 2))
# print(multiply(12, 434, 34, 34, 3))


# =========================================================
# 2. TEXT UTILS MODULE PRACTICE
# =========================================================

# text = "Python is useful for RAG"

# print(text_utils.word_count(text))
# print(text_utils.character_count(text))
# print(text_utils.uppercase(text))


# =========================================================
# 3. BUILT-IN MATH MODULE
# =========================================================

# print(math.sqrt(125))


# =========================================================
# 4. CALCULATOR + EXCEPTION HANDLING
# =========================================================

# try:
#     num1 = float(input("Enter first number: "))
#     operator = input("Enter operation (+, -, *, /): ")
#     num2 = float(input("Enter second number: "))

#     if operator == "+":
#         result = add(num1, num2)
#         print(f"Addition: {result}")

#     elif operator == "-":
#         result = subtact(num1, num2)
#         print(f"Subtraction: {result}")

#     elif operator == "*":
#         result = multiply(num1, num2)
#         print(f"Multiplication: {result}")

#     elif operator == "/":
#         result = divide(num1, num2)
#         print(f"Division: {result}")

#     else:
#         print("Invalid operator")

# except ValueError as error:
#     print(f"Invalid number: {error}")

# except ZeroDivisionError:
#     print("Number cannot be divided by zero")


# =========================================================
# 5. FILE HANDLING
# =========================================================

# try:
#     with open("main.txt", "a", encoding="utf-8") as file:
#         file.write("\nHello, this is Python file handling.")

#     with open("main.txt", "r", encoding="utf-8") as file:
#         for line in file:
#             print(line.strip())

# except OSError as error:
#     print(f"File error: {error}")


# =========================================================
# 6. PATHLIB PRACTICE
# =========================================================


# ---------------------------------------------------------
# File path information
# ---------------------------------------------------------

file_path = Path("/Users/eapple/python/day.py")

print("File name:", file_path.name)
print("File extension:", file_path.suffix)
print("File name without extension:", file_path.stem)


# ---------------------------------------------------------
# Check if file exists
# ---------------------------------------------------------

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")


# ---------------------------------------------------------
# Create a directory
# ---------------------------------------------------------

dir_path = Path("RAG")

dir_path.mkdir(
    parents=True,
    exist_ok=True
)

print("RAG folder is ready")


# ---------------------------------------------------------
# Create nested directories
# ---------------------------------------------------------

nested_dir = Path("RAG") / "Rag1" / "newfolder"

nested_dir.mkdir(
    parents=True,
    exist_ok=True
)

print("Nested folders are ready")


# ---------------------------------------------------------
# iterdir()
# Shows everything directly inside the RAG folder
# ---------------------------------------------------------

present_files = Path("RAG")

print("\n----- Result of iterdir() -----")

for item in present_files.iterdir():
    print(item)


# ---------------------------------------------------------
# glob()
# Shows only PDF files directly inside RAG
# ---------------------------------------------------------

print("\n----- Result of glob() -----")

for pdf_file in present_files.glob("*.pdf"):
    print(pdf_file)