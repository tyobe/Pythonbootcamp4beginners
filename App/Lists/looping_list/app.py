"""
get bank records
get pins
get users
get accounts
"""

import os
os.system('cls')

# get bank records
pins = [111, 222, 333, 444, 555, 777, 888]
users = ["James", "Thandie", "Ivan", "Nelie", "Pastor", "Roland"]
accounts = [1000, 2000, 3000, 4000, 5000, 6000, 7000]

#ATM
enteredPin = int(input ("Enter your pin: "))
index = 0
for pin in pins:
    if(enteredPin == pin):
        print(f"User is{users[index]} and their account balance is ${accounts[index]}")
    index = index + 1

# get accounts with more than $4000
for account in accounts:
    if account >= 4000:
        
