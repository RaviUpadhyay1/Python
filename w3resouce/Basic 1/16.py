# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.
def diff(num):
    if num>17:
        return (num-17)*2
    else:
        return abs(num-17)  
num = int(input("Enter a number:"))  
print(diff(num))                                 
