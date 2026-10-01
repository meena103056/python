students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter student {i + 1} name: ")
    marks = []

    for j in range(3):
        mark = float(input(f"Enter mark for subject {j + 1}: "))
        marks.append(mark)

    total = sum(marks)
    students.append((name, total))

students.sort(key=lambda x: x[1], reverse=True)

print("\n--- Student Ranking ---")

for rank, (name, total) in enumerate(students, start=1):
    print(f"{rank}. {name} - Total Marks: {total}")
