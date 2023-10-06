#Ask user how many grades they would like to enter.
amount = int(input("How many grades would you like to enter?: "))

#Assign grades to values and take user input to calculate GPA.
grades = []
for i in range(amount):
    grade = input("Enter Grade: ")
    if grade.upper() in ["A", "A+"]:
        grades.append(4.0)
    elif grade.upper() in ["A-", "B+"]:
        grades.append(3.7)
    elif grade.upper() in ["B"]:
        grades.append(3.0)
    elif grade.upper() in ["B-", "C+"]:
        grades.append(2.7)
    elif grade.upper() in ["C"]:
        grades.append(2.0)
    elif grade.upper() in ["C-:", "D+"]:
        grades.append(1.7)
    elif grade.upper() in ["D"]:
        grades.append(1.0)
    else:
        grades.append(0.0)

#Calculate GPA 
gpa = sum(grades) / amount

#Display results.
print("GPA=" + str(gpa))





        
        
