from company import Company
import company
from department import Department
from employee import Developer, Manager, Accountant


def main():
    company = Company()
    company.load_data()

    while True:
        print("\n===== COMPANY SYSTEM =====")
        print("1. Shto punonjes")
        print("2. Kerko punonjes")
        print("3. Paga totale")
        print("4. Shiko departamentet")
        print("5. Ruaj te dhenat")
        print("6. Ngarko te dhenat")
        print("0. Dil")

        choice = input("Zgjedh: ")

        if choice == "1":
            emp_id = input("ID: ")
            name = input("Emri: ")
            department_name = input("Departamenti: ")
            employee_type = input(
                "Tipi (Developer/Manager/Accountant): "
            ).lower()

            base_salary = float(input("Paga bazë: "))  # ishte "salary", s'i kalohej fare konstruktorit

            if company.find_department(department_name) is None:
                company.add_department(Department(department_name))

            if employee_type == "developer":
                bonus_rate = float(input("Bonus rate (p.sh. 0.1): "))  # mungonte fare
                employee = Developer(emp_id, name, department_name, base_salary, bonus_rate)
            elif employee_type == "manager":
                team_bonus = float(input("Team bonus: "))
                employee = Manager(emp_id, name, department_name, base_salary, team_bonus)
            elif employee_type == "accountant":
                fixed_bonus = float(input("Fixed bonus: "))
                employee = Accountant(emp_id, name, department_name, base_salary, fixed_bonus)
            else:
                print("Tip i pavlefshem.")
                continue

            try:
                company.add_employee(employee, department_name)
                print("Punonjesi u shtua me sukses.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            emp_id = input("Jep ID-ne e punonjesit: ")
            employee = company.search_employee(emp_id)

            if employee:
                print("Punonjesi u gjet:")
                print(employee)
            else:
                print("Punonjesi nuk u gjet.")

        elif choice == "3":
            print("Paga totale:", company.calculate_total_payroll())

        elif choice == "4":
            if not company.departments:
                print("Nuk ka departamente.")
            else:
                for dept in company.departments:
                    print(f"\nDepartamenti: {dept.name}")
                    for employee in dept.list_employees():
                        print(employee)

        elif choice == "5":
            company.save_data()
            print("Te dhenat u ruajten.")

        elif choice == "6":
            company.load_data()
            print("Te dhenat u ngarkuan.")

        elif choice == "0":
            company.save_data()
            print("Te dhenat u ruajten. Programi u mbyll.")
            break

        else:
            print("Zgjedhje e pavlefshme.")


        if __name__ == "__main__":
            main()

        elif choice == '6':
            emp_id = int(input('Shkruani ID-ne per fshirje: '))
            removed = company.remove_employee(emp_id)
            if removed:
                    print("ID u fshi")
            else:
                  print("ID nuk u fshi")

        elif choice == '7':
             for department in company.departments:
                print(department.name, '-',
                department.py(), 'punonjes')

        elif choice == '8':
            print(company.generate_report())


try:
    base_salary = float(input('Paga baze: '))
    if base_salary < 0:
        print('Paga nuk mund te jete negative.')
        pass
except ValueError:
    print('Ju lutem shkruani nje numer valid.')
    pass
