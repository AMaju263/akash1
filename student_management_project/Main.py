import dataManager
import searchtool
<<<<<<< HEAD
=======
import statistics
>>>>>>> 58c2366d4e931897ae13872c14103fe5813f2d81
print("\nStudent Exam Score Analysis")
print("1. Add student and score")
print("2. Search for student score")
print("3. Display average score for the subject")
print("4. Display all student scores")
print("5. Exit")

choice = input("Choose an option: ")

<<<<<<< HEAD
if choice == 1:
    dataManager.addStudentData()

=======
while choice != 5:
    if choice == 1:
        dataManager.addStudentData()
    
    elif choice == 2:
        searchtool.search()
    elif choice == 3:
        statistics.average
    elif choice == 4:
        searchtool.displayScores
    
>>>>>>> 58c2366d4e931897ae13872c14103fe5813f2d81
