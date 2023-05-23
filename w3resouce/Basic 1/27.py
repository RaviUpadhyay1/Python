# Write a Python program that concatenates all elements in a list into a string and returns it.
# list = [1,2,3,4]
# string = ''
# for element in list:
#     string+=str(element)
# print(string)
#using function
def concatenates(list):
    string = ''
    for element in list:
        string+=str(element)
    return string
list = [1,2,3,4]
print(concatenates(list))
