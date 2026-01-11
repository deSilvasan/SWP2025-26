from __future__ import annotations
import datetime
from enum import Enum

class Genders(Enum):
    male = 0
    female = 1

class Person():
    def __init__(self, name: str, gender: Genders, birthday: datetime.date):
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def __str__(self):
        return f"Ich bin {self.name}, {self.gender} und bin {datetime.datetime.now().date() - self.birthday} Jahre alt."


class Employees(Person):
    def __init__(self, name: str, gender: Genders, birthday: datetime.date, department: Department):
        super().__init__(name, gender, birthday)
        if not isinstance(department, Department):
            raise TypeError("Employee must belong to a Department")
        self.department = department

    def __str__(self):
        return (f"Ich bin {self.name}, {self.gender}, Mitarbeiter der Abteilung {self.department} und bin "
                f"{datetime.datetime.now().date() - self.birthday} Jahre alt.")


class DepartmentManager(Employees):
    def __init__(self, name: str, gender: Genders, birthday:datetime.date, leadingdepartment: Department):
        super().__init__(name, gender, birthday, leadingdepartment)
        self.leadingdepartment = leadingdepartment

    def __str__(self):
        return (f"Ich bin {self.name}, {self.gender}, Abteilungsleister der Abteilung {self.department} und bin "
                f"{datetime.datetime.now().date() - self.birthday} Jahre alt.")


class Department:
    def __init__(self, name: str, leader: DepartmentManager, employees: list):
        self.name = name
        self.leader = leader
        if type(employees) is list:
            self.employees = employees
            self.employees.append(leader)
        else:
            raise TypeError("Department expects a list of Employees in it's constructor")

    def count_emplyees(self):
        return len(self.employees)

    def count_female_employees(self):
        if (len(self.employees) != 0):
            count_female = 0
            for employee in self.employees:
                if employee.gender == Genders.female:
                    count_female += 1
            return count_female
        else:
            raise Exception("There arent existing any employees in the department " + self.name + "!")


class Company:
    def __init__(self, name: str, departments: list):
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
            raise Exception("There arent existing any departments in the company " + self.name + "!")

    def count_departments(self):
        if len(self.departments) != 0:
            total_departments = 0
            for dep in self.departments:
                if (type(dep) == Department):
                    total_departments += 1
            return total_departments
        else:
            raise Exception("There arent existing any departments in the company " + self.name + "!")

    def statistic_department_most_employees(self):
        if len(self.departments) != 0:
            count_dict = {dep.name: dep.count_emplyees() for dep in self.departments}
            return max(count_dict, key=count_dict.get)
        else:
            raise Exception("There arent existing any departments in the company " + self.name + "!")

    def statistic_percentage_female_male(self):
        if len(self.departments) != 0:
            count_female = sum([dep.count_female_employees() for dep in self.departments])
            _, total_employees = self.statistic_employees_departmentmanager()
            return (count_female / total_employees) * 100, ((total_employees - count_female) / total_employees) * 100
        else:
            raise Exception("There arent existing any employees in the company!")

    def __str__(self):
        _, total_employees = self.statistic_employees_departmentmanager()
        department_str = ""
        for dp in self.departments:
            department_str += f"Abteilung {dp.name} mit dem Abteilungsleiter {dp.leader.name}\n"
        return (f"Die Firma {self.name} hat {total_employees} Employees und {len(self.departments)} Departments. "
                f"Die folgenden Abteilungen gibt es: " + department_str)


def main():
    # --- Geburtstage ---
    birthdays = [
        datetime.date(1980, 2, 14),
        datetime.date(1982, 6, 3),
        datetime.date(1985, 12, 25),
        datetime.date(1990, 1, 10),
        datetime.date(1992, 4, 18),
        datetime.date(1995, 9, 30),
        datetime.date(1998, 11, 5),
        datetime.date(1987, 8, 22),
        datetime.date(1991, 3, 12),
        datetime.date(1983, 7, 7),
    ]

    # --- Platzhalter Department für Manager ---
    placeholder_department = Department("Placeholder", None, [])

    # --- Manager erstellen ---
    managers = [
        DepartmentManager("Alice", Genders.male, birthdays[0], placeholder_department),
        DepartmentManager("Bob", Genders.male, birthdays[1], placeholder_department),
        DepartmentManager("Clara", Genders.female, birthdays[2], placeholder_department),
        DepartmentManager("David", Genders.male, birthdays[3], placeholder_department),
    ]

    # --- Mitarbeiter erstellen ---
    employees = [
        Employees("Eve", Genders.female, birthdays[4], placeholder_department),
        Employees("Frank", Genders.male, birthdays[5], placeholder_department),
        Employees("Grace", Genders.female, birthdays[6], placeholder_department),
        Employees("Hank", Genders.male, birthdays[7], placeholder_department),
        Employees("Ivy", Genders.female, birthdays[8], placeholder_department),
        Employees("Jack", Genders.male, birthdays[9], placeholder_department),
    ]

    # --- Departments erstellen ---
    dep1 = Department("IT", managers[0], [employees[0], employees[1]])
    dep2 = Department("HR", managers[1], [employees[2]])
    dep3 = Department("Marketing", managers[2], [employees[3], employees[4]])
    dep4 = Department("Finance", managers[3], [employees[5]])

    # --- Leader mit korrektem Department verknüpfen ---
    for mgr, dep in zip(managers, [dep1, dep2, dep3, dep4]):
        mgr.leadingdepartment = dep
        mgr.department = dep

    # --- Mitarbeiter mit korrektem Department verknüpfen ---
    dep_employees = [dep1.employees, dep2.employees, dep3.employees, dep4.employees]
    for dep_group, dep in zip(dep_employees, [dep1, dep2, dep3, dep4]):
        for emp in dep_group:
            emp.department = dep

    # --- Firma erstellen ---
    my_company = company("TechCorp", [dep1, dep2, dep3, dep4])

    # --- Ausgabe ---
    print(my_company)

    # --- Ausgabe der Firma ---
    print(my_company)

    # --- Statistikmethoden verwenden ---
    print("\n--- Statistik ---")

    # 1. Anzahl Abteilungen und Gesamtanzahl Mitarbeiter
    num_deps, total_emps = my_company.statistic_employees_departmentmanager()
    print(f"Anzahl Departments: {num_deps}")
    print(f"Gesamtanzahl Mitarbeiter: {total_emps}")

    # 2. Abteilung mit den meisten Mitarbeitern
    top_department = my_company.statistic_department_most_employees()
    print(f"Abteilung mit den meisten Mitarbeitern: {top_department}")

    # 3. Prozentuale Verteilung weiblich/männlich
    female_pct, male_pct = my_company.statistic_percentage_female_male()
    print(f"Prozentuale Verteilung: weiblich {female_pct:.1f}%, männlich {male_pct:.1f}%")

    # 4. Anzahl Mitarbeiter pro Abteilung
    for dep in my_company.departments:
        print(
            f"Abteilung {dep.name} hat {dep.count_employees()} Mitarbeiter, davon {dep.count_female_employees()} weiblich.")

if __name__ == '__main__':
    try:
        main()
    except:
        print("An error occured!")
