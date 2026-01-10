from __future__ import annotations
import datetime
from enum import Enum

class Genders(Enum):
    male = 0
    female = 1

class Person():
    def __init__(self, name:str, gender:Genders, birthday: datetime.date):
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def __str__(self):
        return f"Ich bin {self.name}, {self.gender} und bin {datetime.datetime.now().date()-self.birthday} Jahre alt."

class Employees(Person):
    def __init__(self, name:str, gender:Genders, birthday: datetime.date, department:Department):
        super().__init__(name,gender,birthday)
        if not isinstance(department, Department):
            raise TypeError("Employee must belong to a Department")
        self.department = department

    def __str__(self):
        return (f"Ich bin {self.name}, {self.gender}, Mitarbeiter der Abteilung {self.department} und bin "
                f"{datetime.datetime.now().date()-self.birthday} Jahre alt.")

class DepartmentManager(Employees):
    def __init__(self, name: str, gender:Genders, birthday, leadingdepartment:Department):
        super().__init__(name, gender, birthday, leadingdepartment)
        self.leadingdepartment = leadingdepartment

    def __str__(self):
        return (f"Ich bin {self.name}, {self.gender}, Abteilungsleister der Abteilung {self.department} und bin "
                f"{datetime.datetime.now().date()-self.birthday} Jahre alt.")

class Department:
    def __init__(self, name, leader: DepartmentManager, employees: list):
        self.name = name
        self.leader = leader
        if type(employees) is list:
            self.employees = employees
        else:
            raise TypeError("Department expects a list of Employees in it's constructor")

    def count_emplyees(self):
        return len(self.employees)

    def count_female_employees(self):
        if(len(self.employees) != 0):
            count_female = 0
            for employee in self.employees:
                if employee.gender == Genders.female:
                    count_female += 1
            return count_female
        else:
            raise Exception("There arent existing any employees in the department "+self.name+"!")

class company:
    def __init__(self, name:str, departments:list):
        self.name = name
        if type(departments) is list:
            self.departments = departments
        else:
            raise TypeError

    def statistic_employees_departmentmanager(self):
        if len(self.departments) != 0:
            total_employees = [dep.count_emplyees() for dep in self.departments]
            return len(self.departments), sum(total_employees)
        else:
            raise Exception("There arent existing any departments in the company "+self.name+"!")

    def count_departments(self):
        if len(self.departments) != 0:
            total_departments = 0
            for dep in self.departments:
                if (type(dep) == Department):
                    total_departments += 1
            return total_departments
        else:
            raise Exception("There arent existing any departments in the company "+self.name+"!")

    def statistic_department_most_employees(self):
        if len(self.departments) != 0 :
            count_dict = {dep.name: dep.count_emplyees() for dep in self.departments}
            return max(count_dict, key=count_dict.get)
        else:
            raise Exception("There arent existing any departments in the company "+self.name+"!")

    def statistic_percentage_female_male(self):
        if len(self.departments) != 0:
            count_female = sum([dep.count_female_employees() for dep in self.departments])
            _, total_employees = self.statistic_employees_departmentmanager()
            return (count_female / total_employees) * 100, ((total_employees - count_female) / total_employees) * 100
        else:
            raise Exception("There arent existing any employees in the company!")

    def __str__(self):
        department_str = ""
        for dp in self.departments:
            department_str += f"Abteilung {dp.name} mit dem Abteilungsleiter {dp.leader.name}\n"
        return (f"Die Firma {self.name} hat {len(self.employees)} Employees und {len(self.departments)} Departments. "
                f"Die folgenden Abteilungen gibt es: "+ department_str)

if __name__ == '__main__':
    try:
        pass
    except Exception:
        print("An Error happened")