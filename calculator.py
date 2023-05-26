operator = input("enter a operator / + - * %")
num1 = float(input("Enter a number 1"))
num2 = float(input("Enter a number 2"))
if operator == "/":
    Division = num1/num2
    print(Division)
elif operator == "+":
    Sum = num1+num2
    print(Sum)
elif operator == "*":
    Product = num1*num2
    print(Product)
elif operator == "-":
    Subtraction = num1-num2
    print(Subtraction)
elif operator == "%":
    Modulus = num1%num2
    print(Modulus)