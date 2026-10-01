name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))

# Calculate total and average
total = math + science + english + computer
average = total / 4

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Determine pass/fail
if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

# Display results
print("\n===== Student Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 400")
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)

print("==========================")
