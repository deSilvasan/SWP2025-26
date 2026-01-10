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
    def __init__(self, name, leader: DepartmentManager):
        self.name = name
        self.leader = leader

class company:
    def __init__(self, name:str, employees:list, departments:list):
        self.name = name
        if type(employees) is list:
            self.employees = employees
        else:
            raise TypeError
        if type(departments) is list:
            self.departments = departments
        else:
            raise TypeError

    def statistic_employees_departmentmanager(self):
        return len(self.departmentleaders), len(self.employees)

    def count_departments(self):
        return len(self.departments)

    def statistic_department_most_employees(self):
        if self.departments != 0 or len(self.employees) != 0:
            count_dict = {dep.name : 0 for dep in self.departments}
            for employee in self.employees:
                count_dict[employee.department.name] += 1
            return max(count_dict, key=count_dict.get)
        else:
            raise Exception("There arent existing any departments/ employees in the company!")

    def statistic_percentage_female_male(self):
        if len(self.employees) != 0:
            count_female = 0
            for employee in self.employees:
                if employee.gender == Genders.female:
                    count_female += 1
            total_employees = len(self.employees)
            return (count_female / total_employees) * 100, ((total_employees - count_female) / total_employees) * 100
        else:
            raise Exception("There arent existing any employees in the company!")

    def __str__(self):
        department_str = ""
        for dpm in self.departmentleaders:
            department_str += f"Abteilung {dpm.leadingdepartment.name} mit dem Abteilungsleiter {dpm.name}\n"
        return (f"Die Firma {self.name} hat {len(self.employees)} Employees und {len(self.departments)} Departments. "
                f"Die folgenden Abteilungen gibt es: "+ department_str)

if __name__ == '__main__':
    try:
        #Departments
        hr = Department("HR")
        it = Department("IT")
        finance = Department("Finance")

        #Departene Manager
        dm_hr = DepartmentManager(
            name="Anna Berger",
            gender=Genders.female,
            birthday=datetime.date(1985, 4, 12),
            leadingdepartment=hr
        )

        dm_it = DepartmentManager(
            name="Markus Leitner",
            gender=Genders.male,
            birthday=datetime.date(1980, 7, 3),
            leadingdepartment=it
        )

        dm_finance = DepartmentManager(
            name="Julia Kern",
            gender=Genders.female,
            birthday=datetime.date(1988, 11, 22),
            leadingdepartment=finance
        )

        department_managers = [dm_hr, dm_it, dm_finance]

        #Mitarbeiter
        emp1 = Employees(
            name="Max Huber",
            gender=Genders.male,
            birthday=datetime.date(1992, 5, 10),
            department=hr
        )

        emp2 = Employees(
            name="Lisa Gruber",
            gender=Genders.female,
            birthday=datetime.date(1996, 9, 1),
            department=hr
        )

        emp3 = Employees(
            name="Paul Steiner",
            gender=Genders.male,
            birthday=datetime.date(1990, 2, 14),
            department=it
        )

        emp4 = Employees(
            name="Sophie Mayer",
            gender=Genders.female,
            birthday=datetime.date(1994, 12, 8),
            department=finance
        )

        employees = [emp1, emp2, emp3, emp4, department_managers]

        #Company
        schennet_kg = company(
            name="Schennet KG",
            employees=employees,
            departments=[hr, it, finance]
        )

        print(schennet_kg)

        #Statistiken ausgeben
        print("Firma:", schennet_kg.name)

        dm_count, emp_count = schennet_kg.statistic_employees_departmentmanager()
        print(f"Abteilungsleiter: {dm_count}, Mitarbeiter: {emp_count}")

        print("Anzahl Abteilungen:", schennet_kg.count_departments())

        print("Abteilung mit den meisten Mitarbeitern:",
              schennet_kg.statistic_department_most_employees())

        female_pct, male_pct = schennet_kg.statistic_percentage_female_male()
        print(f"Frauen: {female_pct:.1f}%, Männer: {male_pct:.1f}%")

    except Exception:
        print("An Error happened")