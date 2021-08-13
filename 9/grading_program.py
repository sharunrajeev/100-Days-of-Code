student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}


def get_grade(score):
    if score > 90 and score <= 100:
        grade = "Outstanding"
    elif score > 80 and score <= 90:
        grade = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    return grade


for i in student_scores:
    student_grade = get_grade(student_scores[i])
    student_grades[i] = student_grade

print(student_grades)
