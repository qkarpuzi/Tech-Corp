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