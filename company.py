import json
from employee import employee_from_dict
from department import Department


class Company:
    def __init__(self):
        self.departments = []

    def find_department(self, name):
        for d in self.departments:
            if d.name.lower() == name.lower():
                return d
        return None

    def add_department(self, department):
        self.departments.append(department)

    def add_employee(self, employee, department_name):
        dept = self.find_department(department_name)

        if dept is None:
            raise ValueError(f"Departmenti '{department_name}' nuk ekziston.")

        dept.add_employee(employee)

    def search_employee(self, emp_id):
        for dept in self.departments:
            for employee in dept.list_employees():
                if employee.emp_id == emp_id:
                    return employee
        return None

    def calculate_total_payroll(self):
        total = 0

        for dept in self.departments:
            for employee in dept.list_employees():
                total += employee.calculate_salary()

        return total

    def save_data(self, filepath="data.json"):
        data = [d.to_dict() for d in self.departments]

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_data(self, filepath="data.json"):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return

        self.departments = []

        for dept_data in data:
            department = Department(dept_data["name"])

            for employee_data in dept_data.get("employees", []):
                employee = employee_from_dict(employee_data)
                department.add_employee(employee)

            self.departments.append(department)







