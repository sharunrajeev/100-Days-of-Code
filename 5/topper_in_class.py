# Finds topper of the class

student_scores = list(map(int, input("Enter student scores.\n").split()))
high_score = student_scores[0]
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"Highest score is {high_score}")