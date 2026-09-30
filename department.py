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
# 1
    def remove_employee(self, emp_id):
        found = None
        for self.employee in self.employees:
            if self.employee.get_id() == emp_id:
                found = self.employee
                return True
        if found is not None:
            self.employees.remove(found)
            return False
# 2
    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.get_salary()
        return total

    def employee_count(self):
        return len(self.employees)

# 3

    @name.setter
    def name(self, value):
        if value.strip() == '':
             raise ValueError('Emri nuk mund te jete bosh')
        self.__name = value

    def __init__(self, id, name, department, base_salary):
        if id is None or id < 0:
            raise ValueError('ID e pavlefshme')
        self.__id = id

# 4
    def find_by_name(self, name):
        results = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                results.append(employee)
                return results


# 5

from department import Department 
from Employee import Developer, Manager 
it = Department('IT') 
it.add_employee(Developer(1, 'Ajla', 'IT', 1200, 0.1)) 
it.add_employee(Manager(2, 'Omer', 'IT', 1500, 200)) 
print('Total paga:', it.total_salary())  
print('Numri i punonjesve:', it.employee_count()) 
print('Kerkim "ajl":', it.find_by_name('ajl')) 
it.remove_employee(1)
print('Pas fshirjes:', it.employee_count())