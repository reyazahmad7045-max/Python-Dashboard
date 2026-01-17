def calculate_student_performance():
    """
    Calculates and displays total marks, average, and percentage for a student.
    """
    num_subjects = int(input("Enter the number of subjects: "))
    
    marks = []
    total_marks_obtained = 0
    
    for i in range(num_subjects):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i+1} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    total_marks_obtained += mark
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numerical value for marks.")

    max_possible_total_marks = num_subjects * 100

    average_marks = total_marks_obtained / num_subjects
    percentage = (total_marks_obtained / max_possible_total_marks) * 100

    print("\n--- Student Performance Summary ---")
    print(f"Marks entered: {marks}")
    print(f"Total Marks Obtained: {total_marks_obtained:.2f}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Percentage: {percentage:.2f}%")

    # Optional: Assign a simple grade based on percentage
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# Run the program
calculate_student_performance()