class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please enter 1, 2, or 3.")

    def display_employees(self):
        print("Employee ID\tName\tAge\tSalary")
        for emp in self.employees:
            print(emp)

def main():
    database = EmployeeDatabase()

    emp1 = Employee("161E90", "Ramu", 35, 59000)
    emp2 = Employee("171E22", "Tejas", 30, 82100)
    emp3 = Employee("171G55", "Abhi", 25, 100000)
    emp4 = Employee("152K46", "Jaya", 32, 85000)

    database.add_employee(emp1)
    database.add_employee(emp2)
    database.add_employee(emp3)
    database.add_employee(emp4)

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    
    try:
        sorting_param = int(input("Enter your choice (1, 2, or 3): "))
        database.sort_employees(sorting_param)
        database.display_employees()
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
