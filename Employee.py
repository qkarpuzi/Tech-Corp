# 1.
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self, id, name, departament):
        self.__id = id
        self.__name = name
        self.__departament = departament

    @abstractmethod
    def calculate_salary(self):
        pass

# 2.

class Developer(Employee):
    def __init__(self, id, name, departament, bonus_rate):
        super().__init__(id, name, departament)
        self.__bonus_rate = bonus_rate

    def calculate_salary(self):
        return self.__bonus_rate * 1.85

class Manager(Employee):
    def __init__(self, id, name, departament, team_bonus):
        super().__init__(id, name, departament)
        self.__team_bonus = team_bonus

    def calculate_salary(self):
        return self.__team_bonus * 1.85

class Accountat(Employee):
    def __init__(self, id, name, departament, fixed_bonus):
        super().__init__(id, name, departament)
        self.__fixed_bonus = fixed_bonus

    def calculate_salary(self):
        return self.__fixed_bonus * 1.85

#3.
class Employee(ABC):
    @property
    def get_id(self):
        return self.__id

    @brand.setter

    def get_id(self,value):
        if value == "":
            raise ValueError("id nuk mund te jete bosh")
        self.__id = value
        
#5
dev1 = Developer("E 01","Ana","IT",bonus_rate=0.1)
print(dev1.calculate_salary())

dept = Departemnt("IT")
dept.add_employee(dev1)
print(dept.list__employess())

dev2 = Manager("E 02","Ajla","IT",bonus_rate=0.2)
print(dev2.calculate_salary())

dept = Departemnt("IT")
dept.add_employee(dev2)
print(dept.list__employess())

dev3 = Manager("E 03","Era","IT",bonus_rate=0.15)
print(dev3.calculate_salary())

dept = Departemnt("IT")
dept.add_employee(dev3)
print(dept.list__employess())