# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
from datetime import date
f1_date = date(2014, 7, 2)
f2_date = date(2014, 7, 11)
finaldate = f2_date - f1_date
print(finaldate.days)
