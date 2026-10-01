students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter total mark: "))
    students[name] = mark

top_student = max(students, key=students.get)
lowest_student = min(students, key=students.get)

print("\n--- Analysis ---")
print("Top Student:", top_student)
print("Top Mark:", students[top_student])

print("Lowest Student:", lowest_student)
print("Lowest Mark:", students[lowest_student])
