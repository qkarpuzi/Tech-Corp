class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        for e in self.employees:
            if e.get_id == employee.get_id:
                raise ValueError("nje punonjes me kete ID ekziston tashme ketu")
        self.employees.append(employee)

    def list_employees(self):
        return self.employees

    def to_dict(self):
        return {
            "name": self.name,
            "employees": [e.to_dict() for e in self.employees],
        }

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.get_id == emp_id:
                self.employees.remove(employee)
                return True
        return False

    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.calculate_salary()
        return total

    def employee_count(self):
        return len(self.employees)

    def find_by_name(self, name):
        results = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                results.append(employee)
        return results

    def get_highest_paid(self):
        if not self.employees:
            return None
        best = self.employees[0]
        for employee in self.employees:
            if employee.calculate_salary() > best.calculate_salary():
                best = employee
        return best

    def average_salary(self):
        if self.employee_count() == 0:
            return 0
        return self.total_salary() / self.employee_count()
    
    def sort_by_salary(self):
        return sorted(self.employees, key=lambda e:
                      e.calculate_salary(), reverse=True)
    
    def get_lowest_paid(self):
        if not self.employees:
            return None
        return min(self.employees, key=lambda e: e.calculate_salary())