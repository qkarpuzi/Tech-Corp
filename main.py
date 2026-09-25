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
        print("0. Dil")

        choice = input("Zgjedh: ")

        if choice == "1":
            emp_id = input("ID: ")
            name = input("Emri: ")
            department_name = input("Departamenti: ")
            employee_type = input(
                "Tipi (Developer/Manager/Accountant): "
            ).lower()

            salary = float(input("Paga: "))

            if company.find_department(department_name) is None:
                company.add_department(Department(department_name))

            if employee_type == "developer":
                employee = Developer(emp_id, name, salary)
            elif employee_type == "manager":
                employee = Manager(emp_id, name, salary)
            elif employee_type == "accountant":
                employee = Accountant(emp_id, name, salary)
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