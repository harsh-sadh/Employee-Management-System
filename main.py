class Department:
    def __init__(self, dep_id, name):
        self.dep_id = dep_id
        self.name = name

class Employee:
    def __init__(self, emp_id, name, age, position, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.position = position
        self.department = department  # department is a Department object

# ------------------ Management System ------------------

class EmployeeManagementSystem:
    def __init__(self):
        self.departments = []
        self.employees = []

    # ---------- Department Methods ----------
    def add_department(self):
        name = input("Enter department name: ")
        dep_id = len(self.departments) + 1
        self.departments.append(Department(dep_id, name))
        print(f"✅ Department '{name}' added successfully!")

    def view_departments(self):
        if not self.departments:
            print("⚠️ No departments available.")
        else:
            print("\n--- Department List ---")
            for d in self.departments:
                print(f"[{d.dep_id}] {d.name}")

    # ---------- Employee Methods ----------
    def add_employee(self):
        if not self.departments:
            print("⚠️ Please add a department first.")
            return

        name = input("Enter employee name: ")
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("❌ Invalid age.")
            return

        position = input("Enter position: ")

        print("\nAvailable Departments:")
        for d in self.departments:
            print(f"[{d.dep_id}] {d.name}")

        try:
            dep_id = int(input("Enter department ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        department = next((d for d in self.departments if d.dep_id == dep_id), None)
        if not department:
            print("❌ Department not found.")
            return

        emp_id = len(self.employees) + 1
        employee = Employee(emp_id, name, age, position, department)
        self.employees.append(employee)
        print(f"✅ Employee '{name}' added successfully!")

    def view_employees(self):
        if not self.employees:
            print("⚠️ No employees found.")
        else:
            print("\n--- Employee List ---")
            for e in self.employees:
                print(f"[{e.emp_id}] {e.name}, Age: {e.age}, "
                      f"Position: {e.position}, Department: {e.department.name}")

    def delete_employee(self):
        if not self.employees:
            print("⚠️ No employees to delete.")
            return

        try:
            emp_id = int(input("Enter employee ID to delete: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        employee = next((e for e in self.employees if e.emp_id == emp_id), None)
        if employee:
            self.employees.remove(employee)
            print(f"🗑️ Employee '{employee.name}' deleted successfully!")
        else:
            print("❌ Employee not found.")


# ------------------ Main Program ------------------

def main():
    system = EmployeeManagementSystem()

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Department")
        print("2. View Departments")
        print("3. Add Employee")
        print("4. View Employees")
        print("5. Delete Employee")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_department()
        elif choice == "2":
            system.view_departments()
        elif choice == "3":
            system.add_employee()
        elif choice == "4":
            system.view_employees()
        elif choice == "5":
            system.delete_employee()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()