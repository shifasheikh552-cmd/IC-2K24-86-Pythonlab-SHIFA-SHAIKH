# Q1. Student Database using Nested Dictionaries
# Stores: roll_no -> {"name": name, "marks": {subject: score}}

students = {
    "101": {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    "102": {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    "103": {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}}
}


def read_marks():
    """Read and validate marks between 0 and 100."""
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("This roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    marks = {}
    try:
        count = int(input("How many subjects? "))
        if count <= 0:
            print("Enter at least one subject.")
            return
    except ValueError:
        print("Please enter a valid count.")
        return

    for _ in range(count):
        subject = input("Subject name: ").strip()
        if not subject:
            print("Subject name cannot be empty. Try again.")
            continue
        marks[subject] = read_marks()

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")


def update_marks():
    roll = input("Enter roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    subject = input("Enter subject: ").strip()
    if not subject:
        print("Subject cannot be empty.")
        return
    students[roll]["marks"][subject] = read_marks()
    print("Marks updated successfully.")


def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def show_student():
    roll = input("Enter roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    record = students[roll]
    print("\nRoll number:", roll)
    print("Name:", record["name"])
    print("Marks:")
    if record["marks"]:
        for subject, score in record["marks"].items():
            print(f"  {subject}: {score:g}")
    else:
        print("  No marks entered.")


def show_reports():
    if not students:
        print("No student records available.")
        return

    # Calculate each student's average; students with no marks are skipped.
    averages = {
        roll: round(sum(data["marks"].values()) / len(data["marks"]), 2)
        for roll, data in students.items() if data["marks"]
    }

    print("\nAverage marks:")
    if averages:
        for roll, average in averages.items():
            print(f"{roll} - {students[roll]['name']}: {average:.2f}")
        topper_roll = max(averages, key=averages.get)
        print("Topper:", students[topper_roll]["name"], f"({averages[topper_roll]:.2f})")
    else:
        print("No marks available to calculate averages.")

    # Find the highest score separately for every subject.
    subject_scores = {}
    for data in students.values():
        for subject, score in data["marks"].items():
            subject_scores.setdefault(subject, []).append((data["name"], score))

    print("\nHighest scorer in each subject:")
    if subject_scores:
        for subject, scores in subject_scores.items():
            name, score = max(scores, key=lambda item: item[1])
            print(f"{subject}: {name} ({score:g})")
    else:
        print("No subject marks available.")

    print("\nStudents scoring below 40 in at least one subject:")
    found = False
    for roll, data in students.items():
        low_marks = [(subject, score) for subject, score in data["marks"].items() if score < 40]
        if low_marks:
            found = True
            details = ", ".join(f"{subject} {score:g}" for subject, score in low_marks)
            print(f"{data['name']} ({roll}): {details}")
    if not found:
        print("None")

    # Grade is based on the student's average, using the assignment thresholds.
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for roll, average in averages.items():
        name = students[roll]["name"]
        if average >= 90:
            grades["A"].append(name)
        elif average >= 75:
            grades["B"].append(name)
        elif average >= 60:
            grades["C"].append(name)
        elif average >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("\nGrade-wise grouping:")
    print(grades)


def main():
    while True:
        print("\n===== STUDENT DATABASE =====")
        print("1. Add student")
        print("2. Update subject marks")
        print("3. Delete student")
        print("4. Show student record")
        print("5. Reports")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_marks()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            show_student()
        elif choice == "5":
            show_reports()
        elif choice == "6":
            print("Exiting Student Database.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
