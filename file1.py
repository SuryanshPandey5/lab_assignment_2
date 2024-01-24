class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

class EmployeeTable:
    def _init_(self, employees):
        self.employees = employees

    def print_table(self):
        for employee in self.employees:
            print(employee)

    @classmethod
    def sort_table(cls, employees, key):
        try:
            if key == 1:
                return sorted(employees, key=lambda x: x.age)
            elif key == 2:
                return sorted(employees, key=lambda x: x.name)
            elif key == 3:
                return sorted(employees, key=lambda x: x.salary)
            else:
                raise ValueError("Invalid sorting parameter")
        except ValueError as e:
            print(f"Error: {e}")
            return employees

if _name_ == "_main_":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_table = EmployeeTable(employees_data)

    print("Employee Table:")
    employee_table.print_table()

    try:
        sorting_parameter = int(input("\nEnter sorting parameter (1. Age, 2. Name, 3. Salary): "))
        sorted_employees = EmployeeTable.sort_table(employee_table.employees, sorting_parameter)

        print("\nSorted Employee Table:")
        for employee in sorted_employees:
            print(employee)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")