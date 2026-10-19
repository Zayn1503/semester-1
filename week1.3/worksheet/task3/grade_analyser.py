# Ask for the filename once
filename = input("Enter the filename: ")

raw_student_data = []
with open(filename, "r") as file:
    file.readline()  # Skip header line
    for line in file:
        raw_student_data.append(line)

# Clean rows and strip trailing/empty comma values
for i, dat in enumerate(raw_student_data):
    raw_student_data[i] = [item.strip() for item in dat.split(",") if item.strip() != ""]

avg_student_data = []
for student in raw_student_data:
    if len(student) < 2:
        continue

    student_id = student[0]
    total = 0.0
    count = 0

    # Convert each module mark to a float and sum
    for mark in student[1:]:
        total += float(mark)
        count += 1

    average = total / count

    # Grade boundary logic
    if average >= 70:
        grade = "1"
    elif average >= 60:
        grade = "2:1"
    elif average >= 50:
        grade = "2:2"
    elif average >= 40:
        grade = "3"
    else:
        grade = "F"

    avg_student_data.append([student_id, f"{average:.2f}", grade])

# Derive output name automatically from input filename
output_filename = filename + "_out.csv"
with open(output_filename, "w") as file:
    for row in avg_student_data:
        file.write(",".join(row) + "\n")