import os
import datetime   
from playsound import playsound
alarmH = int(input("Hour:"))
alarmM = int(input("Minute:"))
AmorPm = str(input("am or pm: "))
print("Waiting for alarm",alarmH,":",alarmM, AmorPm)
if AmorPm == "pm":
    alarmH +=  12
while True:

    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Time to wake up")
        playsound("D:\Python\Project\Alarm Clock Alarm.mp3")
        break