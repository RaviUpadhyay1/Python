def cm(inch):
    return inch* 2.54
inch = float(input("Enter a number"))
centimeter = cm(inch)
rounded_number = format(centimeter, ".2f")  
# print("The", inch, "= ",%.2f centimeter)\
print("The", inch,"inch", "= ",rounded_number, "centimeters")