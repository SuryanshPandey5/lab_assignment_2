class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id} {self.name} {self.age} {self.salary}"

def sort_employees(employees, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sorting_parameter == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sorting_parameter == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees

def print_employee_data(employees):
    for employee in employees:
        print(employee)

if __name__ == "__main__":
    employee_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    sorting_parameter = int(input("Enter the sorting parameter (1/2/3): "))

    sorted_employees = sort_employees(employee_data, sorting_parameter)
    print("\nSorted Employee Data:")
    print_employee_data(sorted_employees)
