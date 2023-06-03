"""
write a program to check if a year is a leap year
algorithim
get the year
dived year by 4 and keep remainder
check if the remainder is zero then the year is leap year
check if the remainder is not zero then the year is not leap year
"""
import os
os.system ('cls')
 
#get the year 
year = input("Enter year to check: ")
remainder = float(year)%4
if (remainder == 0):
    print(year, "is leap year")
else:
    print(year, "is not leap year")

