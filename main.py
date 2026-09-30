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
        print("7. Fshi punonjes")            # u shtua ne menu
        print("8. Sa punonjes ka çdo departament")   # u shtua ne menu
        print("9. Gjenero raportin e pagave")        # u shtua ne menu
        print("0. Dil")

        choice = input("Zgjedh: ")

        if choice == "1":
            emp_id = int(input("ID: "))          # u rregullua: ishte string, id.__init__ e krahason me < 0
            name = input("Emri: ")
            department_name = input("Departamenti: ")
            employee_type = input("Tipi (Developer/Manager/Accountant): ").lower()

            try:                                    # u shtua: mbrojtje per input jo-numerik ne page
                base_salary = float(input("Paga bazë: "))
                if base_salary < 0:
                    print("Paga nuk mund te jete negative.")
                    continue
            except ValueError:
                print("Ju lutem shkruani nje numer valid.")
                continue

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
            emp_id = int(input("Jep ID-ne e punonjesit: "))   # u rregullua: ishte string
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

        elif choice == "7":                         # u zhvendos ketu: ishte i lidhur gabimisht pas if __name__
            emp_id = int(input("Shkruani ID-ne per fshirje: "))
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
                    print(department.name, "-", department.employee_count(), "punonjes")  # u rregullua: ishte department.py()

        elif choice == "9":
            print(company.generate_report())

        elif choice == "0":
            company.save_data()
            print("Te dhenat u ruajten. Programi u mbyll.")
            break

        else:
            print("Zgjedhje e pavlefshme.")


if __name__ == "__main__":     # u zhvendos: ishte brenda while-loop-it te main(), shkaktonte rekursion te pafund
    main()