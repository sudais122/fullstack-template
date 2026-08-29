from mymath import add,divide,multiply,subtact
import text_utils
import math

# print(add(12,3));
# print(divide(18,2))
# print(multiply(12,434,34,34,3))


import math



text = "Python is useful for RAG"

# print(text_utils.word_count(text))
# print(text_utils.character_count(text))
# print(text_utils.uppercase(text))

print(math.sqrt(125))

num1 = input("enter is number")
op = input("enter opdtion e.g +,-,*,/")
num2 = input("enter second number")

if op == '+':
    result = add(num1,num2)
    print(f"Addintion:${result}")
elif op == '-':
    result = subtact(num1,num2)
    print(f"Subtaction:${result}")
elif op == "*":
    multiply(num1,num2)
else:
    try:
       result = divide(num1,num2)
    except ValueError as error:
        print(error)
    except ZeroDivisionError:
        print("numebr can't divide by zero")
    else:
        print(f"Result:{result}")