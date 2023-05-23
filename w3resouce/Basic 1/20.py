# Write a Python program that returns a string that is n (non-negative integer) copies of a given string
#using function
def larger_string(text,n):
    return text*n
text = input("Enter a text:")    
n = int(input("Enter number of copies:"))
print(larger_string(text.upper(), n))
#without using function
text = input("Enter a text:")    
n = int(input("Enter number of copies:"))
print(text.upper()*n)