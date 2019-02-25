operator = input("what operation do you want to perform?")
num1 = input("what is the first number?")
num2 = input("second number?")

# print(operator)

# if operator == "add" or "addition" or "+":
#     print(int(num1) + int(num2))
if operator == "+":
    print(int(num1) + int(num2))
elif operator == "addition":
    print(int(num1) + int(num2))
elif operator == "add":
    print(int(num1) + int(num2))
elif operator == "-":
    print(int(num1)- int(num2))
elif operator == "subtraction":
    print(int(num1)- int(num2))
elif operator == "subtract":
    print(int(num1)- int(num2))
elif operator == "divide":
    print(int(num1) // int(num2))
elif operator == "division":
    print(int(num1) // int(num2))
elif operator == "/":
    print(int(num1) // int(num2))
elif operator == "*":
    print(int(num1) * int(num2))
elif operator == "multiplication":
    print(int(num1) * int(num2))
elif operator == "multiply":
    print(int(num1) * int(num2))
elif operator == "exponent":
    print(int(num1) ** int(num2))
else:
    print ("unrecognized input")