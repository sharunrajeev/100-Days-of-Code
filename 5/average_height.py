# Average height calculator
# Uses for loops

student_height = list(
    map(int, input("Enter the heights of students: ").split()))
sum = 0
for i in student_height:
    sum += i
print(sum // len(student_height)) # floors the result
