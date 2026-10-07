from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id, name, departament, base_salary):
        self.__id = id
        self.__name = name
        self.__departament = departament
        self.__base_salary = base_salary

    @property
    def name(self):
        return self.__name

    @property
    def departament(self):
        return self.__departament

    @property
    def base_salary(self):
        return self.__base_salary

    @property
    def get_id(self):
        return self.__id

    @get_id.setter
    def get_id(self, value):
        if value == "":
            raise ValueError("id nuk mund te jete bosh")
        self.__id = value

    @abstractmethod
    def calculate_salary(self):
        pass

    def give_raise(self, percentage):
        if percentage < 0:
            raise ValueError('Perqindja nuk mund te jete negative')
        new_salary = self.__base_salary + (self.__base_salary * percentage)
        self.__base_salary = new_salary

    def __str__(self):
        return f"[{self.get_id}] {self.__name} - {self.__departament}"

    def to_dict(self):
        return {
            "type": type(self).__name__,
            "id": self.get_id,
            "name": self.__name,
            "departament": self.__departament,
            "base_salary": self.__base_salary,
        }


class Developer(Employee):
    def __init__(self, id, name, departament, base_salary, bonus_rate):
        super().__init__(id, name, departament, base_salary)
        if bonus_rate < 0 or bonus_rate > 1:
            raise ValueError("bonus_rate duhet te jete 0-1")
        self.__bonus_rate = bonus_rate

    def calculate_salary(self):
        return self.base_salary + (self.base_salary * self.__bonus_rate)

    def to_dict(self):
        d = super().to_dict()
        d["bonus_rate"] = self.__bonus_rate
        return d


class Manager(Employee):
    def __init__(self, id, name, departament, base_salary, team_bonus):
        super().__init__(id, name, departament, base_salary)
        self.__team_bonus = team_bonus

    def calculate_salary(self):
        return self.base_salary + self.__team_bonus

    def to_dict(self):
        d = super().to_dict()
        d["team_bonus"] = self.__team_bonus
        return d


class Accountant(Employee):
    def __init__(self, id, name, departament, base_salary, fixed_bonus):
        super().__init__(id, name, departament, base_salary)
        self.__fixed_bonus = fixed_bonus

    def calculate_salary(self):
        return self.base_salary + self.__fixed_bonus

    def to_dict(self):
        d = super().to_dict()
        d["fixed_bonus"] = self.__fixed_bonus
        return d


def employee_from_dict(data):
    t = data["type"]
    if t == "Developer":
        return Developer(data["id"], data["name"], data["departament"], data["base_salary"], data["bonus_rate"])
    elif t == "Manager":
        return Manager(data["id"], data["name"], data["departament"], data["base_salary"], data["team_bonus"])
    elif t == "Accountant":
        return Accountant(data["id"], data["name"], data["departament"], data["base_salary"], data["fixed_bonus"])
    else:
        raise ValueError(f"tip i panjohur: {t}")


if __name__ == "__main__":
    dev1 = Developer("E01", "Ana", "IT", 1000, bonus_rate=0.1)
    print(dev1.calculate_salary())

    from department import Department

    dept = Department("IT")
    dept.add_employee(dev1)
    print(dept.list_employees())

    dev2 = Manager("E02", "Ajla", "IT", 1200, team_bonus=200)
    print(dev2.calculate_salary())
    dept.add_employee(dev2)
    print(dept.list_employees())

    dev3 = Manager("E03", "Era", "IT", 1100, team_bonus=150)
    print(dev3.calculate_salary())
    dept.add_employee(dev3)
    print(dept.list_employees())

    @name.setter
    def name(self,value):
        if value.strip() == "":
            raise ValueError('emri nuk  mund te jete bosh')
        self._name = value

    def __init__(self,id,name,departament,base_salary):
        self.__id = id
        self.__name = name
        self.__departament = departament
        self.__base_salary = base_salary