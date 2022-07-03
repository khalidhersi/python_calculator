# Input variables
number_1 = input("Enter A Number: ")
operator_sign = input("Enter An Operator: ")
number_2 = input("Enter A 2nd Number: ")


# Calculation Logic Function
def calculator(num1, operator, num2):
    if operator == "*":
        return float(num1) * float(num2)
    elif operator == "/":
        return float(num1) / float(num2)
    elif operator == "+":
        return float(num1) + float(num2)
    elif operator == "-":
        return float(num1) - float(num2)
    else:
        print("Syntax Error: Please Enter A Valid Entry")


# Calling & Printing Calculator Function
print(calculator(number_1, operator_sign, number_2))
