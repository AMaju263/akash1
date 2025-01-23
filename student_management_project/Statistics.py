def calculate_average(scores):
    if len(scores) > 0:
        return sum(scores) / len(scores)
    else:
        return 0 


def average(student_scores) :

    # Calculate and display the average score
    if student_scores:
        average_score = calculate_average(list(student_scores.values()))
        print(f"The average score of all students in the exam is: {average_score:.2f}")
    else:
        print("No students' data available.")