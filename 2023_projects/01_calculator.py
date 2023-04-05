operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter 1st value: "))
num2 = float(input("Enter 2nd value: "))

if operator == "+":
    result = num1 + num2
    print(f"Result is {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"Result is {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"Result is {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"Result is {round(result, 3)}")
else:
    print(f"Operator {operator} is not valid!")