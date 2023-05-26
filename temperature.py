print("press 1 for celcius to farenheit")
print("press 2 for celcius to kelvin")
print("press 3 for farenheit to celcius")
print("press 4 for farenheit to kelvin")
print("press 5 for kelvin to farenheit")
print("press 6 for kelvin to celcius ")
unit = int(input("Enter a no. from which to which temperature u want to change:"))
temp =float5(input("Enter the temperature value:"))
if unit ==1:
    temp = round((temp * 9/5) + 32,2)
    print(f"The temperature in farenheit is {temp}")
elif unit == 2:
    temp = round((temp + 273.15),2)
elif unit==3:
    temp ==  round([(temp-32)*5]/9,2)
    print(f"The temperature in celcius is {temp}")
elif unit==4:
    temp= round(1.8*(temp-273) + 32,2)
    print(f"The temperatur in  farenheit is{temp}")
elif unit==5:
    temp = round((temp - 273.15) * 9/5 + 32,2)
    print(f"The temperatur in farenheit is{temp} ")
elif unit==6:
    temp = round(temp - 273.15,2)
else:
    print("Invalid input")