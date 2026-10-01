n = int(input("Enter number of students: "))

excellent = []
average_students = []
weak = []

for i in range(n):
    name = input(f"\nEnter student {i + 1} name: ")
    mark = float(input("Enter average mark: "))

    if mark >= 80:
        excellent.append(name)
    elif mark >= 50:
        average_students.append(name)
    else:
        weak.append(name)

print("\n--- Performance Analysis ---")

print("\nExcellent Students:")
for name in excellent:
    print(name)

print("\nAverage Students:")
for name in average_students:
    print(name)

print("\nStudents Requiring Improvement:")
for name in weak:
    print(name)
