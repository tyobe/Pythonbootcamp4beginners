"""
Checking for eligible students to graduate
algorithim
create lists of students names and classes
get students grades in Computer Science
get students grades in Data Science
get students grades in Mathematics
Testing the grading for graduation
Generate reports
"""

import os
os.system ('cls')
# Create lists for names and classes
studentNames = ["Emma Thompson", "Ethan Martinez", "Isabella Rodriguez", 
                "William Martinez", "Olivia Moore", "Emma Walker", 
                "Oliver Hernandez", "Ava Anderson", "Olivia Martin"]
computerScienceGrades = [85, 72, 94, 89, 84, 92, 91, 90, 85,]
dataScienceGrades = [92, 91, 70, 92, 90, 83, 82, 88, 53]
mathmeticsGrades = [78, 83, 88, 85, 65, 95, 66, 91, 78]

#a list for graduating students
for index in range(len(studentNames)):
#    print (f"{index} - {studentNames[index]} - CS: {computerScienceGrades[index]}% - DS: {dataScienceGrades[index]}% - M: {mathmeticsGrades[index]}%")
    graduationStatus = True
    # Computer Science Grades
    print()
    if(computerScienceGrades[index] >= 90 and computerScienceGrades[index] <= 100):
        print(f"{studentNames[index]} - CS Score: A")
    elif(computerScienceGrades[index] >= 80 and computerScienceGrades[index] <= 89):
        print(f"{studentNames[index]} - CS Score: B")
    elif(computerScienceGrades[index] >= 70 and computerScienceGrades[index] <= 79):
        print(f"{studentNames[index]} - CS Score: C")
        graduationStatus = False
    elif(computerScienceGrades[index] >= 60 and computerScienceGrades[index] <= 69):
        print(f"{studentNames[index]} - CS Score: D")
        graduationStatus = False
    else:
        print(f"{studentNames[index]} - CS Score: F")
        graduationStatus = False
    # Data Science Grades
    print()
    if(dataScienceGrades[index] >= 90 and dataScienceGrades[index] <= 100):
        print(f"{studentNames[index]} - DS Score: A")
    elif(dataScienceGrades[index] >= 80 and dataScienceGrades[index] <= 89):
        print(f"{studentNames[index]} - DS Score: B")
    elif(dataScienceGrades[index] >= 70 and dataScienceGrades[index] <= 79):
        print(f"{studentNames[index]} - DS Score: C")
        graduationStatus = False
    elif(dataScienceGrades[index] >= 60 and dataScienceGrades[index] <= 69):
        print(f"{studentNames[index]} - DS Score: D")
        graduationStatus = False
    else:
        print(f"{studentNames[index]} - DS Score: F")
        graduationStatus = False
    # Mathmetics Grades
    print()
    if(mathmeticsGrades[index] >= 90 and mathmeticsGrades[index] <= 100):
        print(f"{studentNames[index]} - M Score: A")
    elif(mathmeticsGrades[index] >= 80 and mathmeticsGrades[index] <= 89):
        print(f"{studentNames[index]} - M Score: B")
    elif(mathmeticsGrades[index] >= 70 and mathmeticsGrades[index] <= 79):
        print(f"{studentNames[index]} - M Score: C")
    elif(mathmeticsGrades[index] >= 60 and mathmeticsGrades[index] <= 69):
        print(f"{studentNames[index]} - M Score: D")
        graduationStatus = False
    else:
        print(f"{studentNames[index]} - M Score: F")
        graduationStatus = False

    print(f"{studentNames[index]} - Graduation status: {graduationStatus}")
#students with a score greater than 79 in computer science class
print(f"/n/nstudents with a score greater than 79 in computer science class: /n")

if graduationStatus == True:
    graduatingStudentList.append(studentNames(index))

for index in range (len(mathmeticsGrades)):
    if mathmeticsGrades[index] >79:
        print((f"{studentNames[index]} - Math Grade: {mathmeticsGrades[index]}"))