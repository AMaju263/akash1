# Function to calculate the average score of multiple students
def calculate_average(scores):
    if len(scores) > 0:
        return sum(scores) / len(scores)
    else:
        return 0
    


# Main program to input data and calculate the average score
def main():
    student_scores = {}  # Dictionary to store student names and their scores in the subject
    while True:
        # Menu for user
        print("\nStudent Exam Score Analysis")
        print("1. Add student and score")
        print("2. Search for student score")
        print("3. Display average score for the subject")
        print("4. Display all student scores")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            # Add student and score
            name = input("Enter student's name: ")
            score = float(input("Enter student's score: "))
            student_scores[name] = score
            print(f"Added {name} with score {score}")
        
        elif choice == '2':
            # Search for student score
            name = input("Enter student's name to search: ")
            if name in student_scores:
                print(f"{name}'s score: {student_scores[name]}")
            else:
                print(f"No record found for {name}.")
        
        elif choice == '3':
            # Calculate and display the average score
            if student_scores:
                average_score = calculate_average(list(student_scores.values()))
                print(f"The average score of all students in the exam is: {average_score:.2f}")
            else:
                print("No students' data available.")
        
        elif choice == '4':
            # Display all students and their scores
            if student_scores:
                print("\nAll students and their scores in the exam:")
                for name, score in student_scores.items():
                    print(f"{name}: {score}")
            else:
                print("No students' data available.")
        
        elif choice == '5':
            # Exit the program
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

student_scores = {}  # Dictionary to store student names and their scores in the subject

def search():
    name = input("Enter student's name to search: ")
    if name in student_scores:
            print(f"{name}'s score: {student_scores[name]}")
    else:
            print(f"No record found for {name}.")

def displayScores():
    
            # Display all students and their scores
            if student_scores:
                print("\nAll students and their scores in the exam:")
                for name, score in student_scores.items():
                    print(f"{name}: {score}")
            else:
                print("No students' data available.")