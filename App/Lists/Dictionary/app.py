


import os
os.system

studentList = [
    {
        "name": "Emma Thompson",
        "csGrade": 85,
        "dsGrade": 92,
        "math": 78,
    },
    {
        "name": "Ethan Martinez",
        "csGrade": 72,
        "dsGrade": 91,
        "math": 83,
    },
    {
        "name": "Isabella Rodriguez",
        "csGrade": 94,
        "dsGrade": 70,
        "math": 85,
    },
    {
        "name": "William Martinez",
        "csGrade": 89,
        "dsGrade": 92,
        "math": 88,
    },
    {
        "name": "Olivia Moore",
        "csGrade": 84,
        "dsGrade": 90,
        "math": 65,
    },
    {
        "name": "Emma Walker",
        "csGrade": 92,
        "dsGrade": 83,
        "math": 95,
    },
    {
        "name": "Oliver Hernandez",
        "csGrade": 91,
        "dsGrade": 82,
        "math": 66,
    },
    {
        "name": "Ava Anderson",
        "csGrade": 90,
        "dsGrade": 88,
        "math": 91,
    },
    {
        "name": "Olivia Martin",
        "csGrade": 85,
        "dsGrade": 53,
        "math": 78,
    }
]
#studentList[5]["csGrade"] = 90
#for student in studentList:
# studentList[5].update({"csGrade": 90})
# studentList[5]["Art"] = 90 
# studentList[5].update({"English": 99})

# print(studentList[5])
# for studentDict in studentList:
#    if(studentDict["csGrade"] > 79 and  studentDict["dsGrade"] > 79 and studentDict["math"] > 69):
#     #   studentDict["gradStatus"] = True
#     studentDict.update({"gradStatus": True})
#    else:
#       studentDict["gradStatus"] = False
#    print(f'\n{studentDict["name"]} \nCS : {studentDict["csGrade"]} DS : {studentDict["dsGrade"]} Math : {studentDict["math"]}  \nStatus : {studentDict["gradStatus"]}')

# for studentDict in studentList:
#   for key in studentDict:
#     #print(item)
#     print(studentDict[key])
for studentDict in studentList:
    for key, value in studentDict.items():
        print(key, value)


# print(f'{student["name"]} CS : {student["csGrade"]} DS : {student["dsGrade"]} Math : {student["math"]}')
# print(f'{student1["name"]} CS : {student1["csGrade"]} DS : {student1["dsGrade"]} Math : {student1["math"]}')
# print(f'{student1.get("name")} CS : {student1.get("csGrade")} DS : {student1.get("dsGrade")} Math : {student1.get("math")}') 
