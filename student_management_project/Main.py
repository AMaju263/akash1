import dataManager
import searchtool
import statistics
print("\nStudent Exam Score Analysis")
print("1. Add student and score")
print("2. Search for student score")
print("3. Display average score for the subject")
print("4. Display all student scores")
print("5. Exit")

choice = input("Choose an option: ")

while choice != 5:
    if choice == 1:
        dataManager.addStudentData()
    
    elif choice == 2:
        searchtool.search()
    elif choice == 3:
        statistics.average
    elif choice == 4:
        searchtool.displayScores
    