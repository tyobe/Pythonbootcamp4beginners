"""
Write a program to check if the number is odd or even
Algorithim
Get a number
Dived number by 2 and keep remainder
Check if remainder if zero then number is even
Check if remainder is not zero then number is odd
"""

#get number
number = input("Enter number to check: ")
remainder = float(number)%2
if (remainder == 0):
    print(number, " is even")
else:
    print(number, " is odd")




    