#changing the year value from 1964 to 2020 of a car

import os
os.system

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 

#Change the "year" value from 1964 to 2020
car.update({"year": 2020})
print(car)

#Add the key/value pair "color" : "red" to the car dictionary
car.update({"color": "red"})
print(car)

#Use the pop method to remove "model" from the car dictionary.

car.pop("model")
print(car)