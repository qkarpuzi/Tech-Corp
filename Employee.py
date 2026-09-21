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
        self.__tem_bonus = team_bonus

    def calculate_salary(self):
        return self.__team_bonus * 1.85

class Accountat(Employee):
    def __init__(self, id, name, departament, fixed_bonus):
        super().__init__(id, name, departament)
        self.__fixed_bonus = fixed_bonus

    def calculate_salary(self):
        return self.__fixed_bonus * 1.85