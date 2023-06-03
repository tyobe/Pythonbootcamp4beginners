"""
Multiple conditions example: 
 Assume a bank has 3 types of accounts, 
 student account for students, professional account for the working class, 
 and retirement account for retirees.  You can only open an account if you are 18 years or order.
"""
import os
os.system("cls")

clientOccupation = input("Enter client occupatiStudenton:(Student/Professional/Retiree ): ")
clientAge = input ("Enter age: ")

if (clientOccupation == "Student" and int(clientAge) >= 18 ):
   print("Get a Student account")
elif (clientOccupation == "Professional" and int(clientAge) >= 18 ):
    print("Get a Professional account")
elif (clientOccupation == "Retiree" and int(clientAge) >= 18 ):
    print("Get a Retirement account")
else:
    print( "There is no account available for this client")