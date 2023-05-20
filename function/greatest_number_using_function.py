def greatest(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
a = int(input("Enter a number 1:"))
b = int(input("Enter a number 2:"))
c = int(input("Enter a number 3:"))
great = greatest(a,b,c)
print("The maximum number is ", great)
