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
        found = None
        for employee in self.employees:          # u rregullua: ishte "self.employee", krijonte atribut te panevojshem
            if employee.get_id == emp_id:         # u rregullua: get_id eshte @property, s'therritet me ()
                found = employee
                break                              # u shtua: ndalon loop-in sapo gjendet
        if found is not None:
            self.employees.remove(found)
            return True                            # u zhvendos: tani fshihet PARA se te kthehet True
        return False                               # u rregullua: ishte i paarritshem, tani ekzekutohet gjithmone ne rastin "s'u gjet"

    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.calculate_salary()   # u rregullua: get_salary() s'ekzistonte fare
        return total

    def employee_count(self):
        return len(self.employees)

    def find_by_name(self, name):
        results = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                results.append(employee)
        return results                              # u rregullua: ishte brenda for-it, kthente vetem 1 rezultat