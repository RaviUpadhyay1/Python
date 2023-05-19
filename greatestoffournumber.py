num1 = int(input("Enter a number 1:"))
num2 = int(input("Enter a number 2:"))
num3 = int(input("Enter a number 3:"))
num4 = int(input("Enter a number 4:"))
if(num1>num2 and num1>num3 and num1>num4):
    print(num1)
elif(num2>num3 and num2>num4 and num2>num1  ):
    print(num2)
elif(num3>num4 and num3>num2 and num3>num1  ):
    print(num3)
else:
    print(num4)


# Using function
# def find_greatest(a, b, c, d):
#     # Initialize the maximum variable with the first number
#     maximum = a

#     # Compare the remaining numbers with the current maximum
#     if b > maximum:
#         maximum = b
#     if c > maximum:
#         maximum = c
#     if d > maximum:
#         maximum = d
#     return maximum
# # Test the function
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the fourth number: "))

# result = find_greatest(num1, num2, num3, num4)
# print("The greatest number is:", result)
