# Q2. Employee Database using Dictionaries
# Stores: emp_id -> {"name": name, "dept": department, "salary": salary}

employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000.0},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000.0},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000.0},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000.0},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000.0}
}


def read_salary():
    while True:
        try:
            salary = float(input("Enter salary: "))
            if salary >= 0:
                return salary
            print("Salary cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def add_employee():
    emp_id = input("Enter employee ID: ").strip()
    if emp_id in employees:
        print("Employee ID already exists.")
        return
    name = input("Enter employee name: ").strip()
    dept = input("Enter department: ").strip()
    if not name or not dept:
        print("Name and department cannot be empty.")
        return
    employees[emp_id] = {"name": name, "dept": dept, "salary": read_salary()}
    print("Employee added successfully.")


def update_salary():
    emp_id = input("Enter employee ID: ").strip()
    if emp_id not in employees:
        print("Employee not found.")
        return
    employees[emp_id]["salary"] = read_salary()
    print("Salary updated successfully.")


def delete_employee():
    emp_id = input("Enter employee ID to delete: ").strip()
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def search_employee():
    emp_id = input("Enter employee ID: ").strip()
    if emp_id in employees:
        print(emp_id, ":", employees[emp_id])
    else:
        print("Employee not found.")


def show_reports():
    if not employees:
        print("No employee records available.")
        return

    # Build payroll totals and headcounts together in one pass.
    department_data = {}
    for data in employees.values():
        dept = data["dept"]
        if dept not in department_data:
            department_data[dept] = {"payroll": 0, "headcount": 0}
        department_data[dept]["payroll"] += data["salary"]
        department_data[dept]["headcount"] += 1

    print("\nDepartment-wise payroll and headcount:")
    for dept, info in department_data.items():
        print(f"{dept}: payroll = {info['payroll']:.2f}, headcount = {info['headcount']}")

    print("\nHighest-paid employee in each department:")
    highest_by_dept = {}
    for emp_id, data in employees.items():
        dept = data["dept"]
        if dept not in highest_by_dept or data["salary"] > highest_by_dept[dept][1]:
            highest_by_dept[dept] = (data["name"], data["salary"])
    for dept, (name, salary) in highest_by_dept.items():
        print(f"{dept}: {name} ({salary:.2f})")

    print("\nEmployees sorted by salary (highest first):")
    for emp_id, data in sorted(employees.items(),
                               key=lambda item: item[1]["salary"], reverse=True):
        print(f"{emp_id}: {data['name']} - {data['salary']:.2f}")

    # Create a separate dictionary so the original employee salaries are not changed.
    # This is safer because a report should calculate proposed raises without
    # permanently modifying the actual database records.
    raised_employees = {
        emp_id: {
            **data,
            "salary": data["salary"] * 1.10 if data["salary"] < 50000 else data["salary"]
        }
        for emp_id, data in employees.items()
    }

    print("\nNew dictionary after 10% raise for salaries below 50000:")
    for emp_id, data in raised_employees.items():
        if employees[emp_id]["salary"] < 50000:
            print(f"{data['name']}: {data['salary']:.2f}")
    print("Original salaries remain unchanged.")

    average_by_dept = {
        dept: info["payroll"] / info["headcount"]
        for dept, info in department_data.items()
    }
    best_dept = max(average_by_dept, key=average_by_dept.get)
    print(f"\nDepartment with highest average salary: {best_dept} "
          f"({average_by_dept[best_dept]:.2f})")


def main():
    while True:
        print("\n===== EMPLOYEE DATABASE =====")
        print("1. Add employee")
        print("2. Update salary")
        print("3. Delete employee")
        print("4. Search by ID")
        print("5. Reports")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            update_salary()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            show_reports()
        elif choice == "6":
            print("Exiting Employee Database.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
