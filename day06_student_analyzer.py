
import json


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


try:
    inp1 = int(input("Enter Python marks: "))
    inp2 = int(input("Enter Math marks: "))
    inp3 = int(input("Enter AI marks: "))

    total_marks = calculate_total([inp1, inp2, inp3])
    average = calculate_average([inp1, inp2, inp3])

    print("you entered marks for Python:", inp1)
    print("you entered marks for Math:", inp2)
    print("you entered marks for AI:", inp3)
    print("Total Marks:", total_marks)
    print("Average:", average)

    grade = calculate_grade(average)
    print("Grade:", grade)

    result = {
        "python": inp1,
        "math": inp2,
        "ai": inp3,
        "total": total_marks,
        "average": average,
        "grade": grade
    }

    print("Data saved to student_marks.json")

    with open("student_marks.json", "w") as file:
        json.dump({
            "Python": inp1,
            "Math": inp2,
            "AI": inp3,
            "Total Marks": total_marks,
            "Average": average,
            "Grade": grade
        }, file, indent=4)

except ValueError:
    print("Invalid input. Please enter valid integer marks.")

   