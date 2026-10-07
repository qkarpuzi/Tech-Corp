from company import Company
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
        print("7. Fshi punonjes")
        print("8. Numri i punonjesve per departament")
        print("9. Raporti i pagave")
        print("10. Jep rritje page")
        print("11. Punonjesi me i lartepaguar")
        print("12. Eksporto raportin ne file")
        print("0. Dil")

        choice = input("Zgjedh: ")

        if choice == "1":
            try:
                emp_id = int(input("ID: "))
            except ValueError:
                print("ID duhet te jete numer.")
                continue
            name = input("Emri: ")
            department_name = input("Departamenti: ")
            employee_type = input("Tipi (Developer/Manager/Accountant): ").lower()
            base_salary = float(input("Paga baze: "))

            if company.find_department(department_name) is None:
                company.add_department(Department(department_name))

            if employee_type == "developer":
                bonus_rate = float(input("Bonus rate (p.sh. 0.1): "))
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
            try:
                emp_id = int(input("Jep ID-ne e punonjesit: "))
            except ValueError:
                print("ID duhet te jete numer.")
                continue
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

        elif choice == "7":
            try:
                emp_id = int(input("Shkruani ID-ne per fshirje: "))
            except ValueError:
                print("ID duhet te jete numer.")
                continue
            removed = company.remove_employee(emp_id)
            if removed:
                print("Punonjesi u fshi me sukses.")
            else:
                print("ID nuk u gjet.")

        elif choice == "8":
            if not company.departments:
                print("Nuk ka departamente.")
            else:
                for department in company.departments:
                    print(department.name, "-", department.employee_count(), "punonjes")

        elif choice == "9":
            print(company.generate_report())

        elif choice == '10':
            try:
                emp_id = int(input('ID e punonjesit: '))
            except ValueError:
                print("ID duhet te jete numer.")
                continue
            employee = company.search_employee(emp_id)
            if employee is None:
                print('Punonjesi nuk u gjet.')
                continue
            try:
                percentage = float(input('Perqindja e rritjes (p.sh. 0.1): '))
                employee.give_raise(percentage)
                print('Paga e re:', employee.base_salary)
            except ValueError as e:
                print(e)

        elif choice == '11':
            top = company.get_top_earner()
            if top is None:
                print('Nuk ka ende punonjes ne sistem.')
            else:
                print(top.name, '-', top.calculate_salary())

        elif choice == '12':
            company.export_report_to_file('raporti.txt')
            print('Raporti u ruajt ne raporti.txt')

        elif choice == "0":
            company.save_data()
            print("Te dhenat u ruajten. Programi u mbyll.")
            break

        else:
            print("Opsion i pavlefshem.")


if __name__ == "__main__":
    main()