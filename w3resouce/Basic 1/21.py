#  Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
#  and prints an appropriate message to the user.
# num = int(input("Enter a number:"))
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")
# using function
def oddeven(n):
    if n%2==0:
        print(n,"is an even number")
    else:
        print(n,"is an odd number")   
n = int(input("Enter a number:"))
oddeven(n)