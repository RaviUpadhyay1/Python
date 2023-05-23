import datetime
import nepali_datetime 
print("Current date and time:",datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S %p"))
print("Current date and time:",nepali_datetime.datetime.now().strftime("%d-%B-%Y %H:%M %p"))
print("Current date and time in nepali:",nepali_datetime.datetime.now().strftime('%K-%N-%G %h:%l %p'))