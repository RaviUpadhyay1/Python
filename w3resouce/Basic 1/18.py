# Write a Python program to calculate the sum of three given numbers.
#  If the values are equal, return three times their sum.
num1 = int(input("Enter a number 1:"))
num2 = int(input("Enter a number 2:"))
num3 = int(input("Enter a number 3:"))
if (num1==num2==num3):
    sum = 3*(num1+num2+num3)
    print(sum)
else:
    sum = num1+num2+num3
    print(sum)