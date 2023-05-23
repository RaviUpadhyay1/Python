# Write a Python program that checks whether a specified value is contained within a group of values.?
# value = input("Enter a value:")
# group_value = "ravi"
# if value in group_value:
#     print("value is in group value")
# else:
    # print("value is not in group value")
#using function
def check_value(value,group_value):
    if value in group_value:
        print("value is in group value")
    else:
        print("value is not in group value")
value = input("enter a value:")
group_value = input("enter a group_value:")
check_value(value,group_value)