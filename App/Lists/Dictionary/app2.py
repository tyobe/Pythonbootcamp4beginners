#changing the year value from 1964 to 2020 of a car

import os
os.system

car = [	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} ]

#Change the "year" value from 1964 to 2020
car[0].update({"year": 2020})
print(car[0])

#Add the key/value pair "color" : "red" to the car dictionary
car[0].update({"color": "red"})
print(car[0])

#Use the pop method to remove "model" from the car dictionary.
for carDict in car:
    carDict.pop("model")
    print(carDict)