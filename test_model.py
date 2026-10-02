from department import Department
from Employee import Developer, Manager

it = Department('IT')
it.add_employee(Developer(1, 'Ajla', 'IT', 1000, 0.1))
it.add_employee(Manager(2, 'Omer', 'IT', 1500, 200))

it.employees[0].give_raise(0.1)
print('Pas rritjes:', it.employees[0].base_salary)
print('Me i larti:', it.get_highest_paid().name)
print('Mesatarja:', it.average_salary())