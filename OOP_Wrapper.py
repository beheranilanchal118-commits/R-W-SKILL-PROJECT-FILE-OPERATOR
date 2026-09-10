# ==========================================================
#          PYTHON OOP PROJECT: EMPLOYEE MANAGEMENT SYSTEM
# ==========================================================


# ------------------------- EMPLOYEE CLASS -------------------------

class Employee:

    def __init__(self, employee_id=None, name=None, age=0, salary=0):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    # ------------------------- CLASS METHOD -------------------------

    @classmethod
    def from_values(cls, employee_id, name, age, salary):
        return cls(employee_id, name, age, salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # ------------------------- __STR__ METHOD -------------------------

    def __str__(self):
        return (
            f"Employee ID: {self.__employee_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Salary: {self.__salary}"
        )

    def display(self):
        print(f"Employee ID : {self.__employee_id}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Salary      : {self.__salary}")

    # ------------------------- DESTRUCTOR -------------------------

    def __del__(self):
        print("Object is destroyed")


# ------------------------- MANAGER CLASS -------------------------

class Manager(Employee):

    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department  : {self.department}")


# ------------------------- DEVELOPER CLASS -------------------------

class Developer(Employee):

    def __init__(
        self,
        employee_id,
        name,
        age,
        salary,
        department,
        programming_language
    ):
        super().__init__(employee_id, name, age, salary)
        self.department = department
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Department  : {self.department}")
        print(
            f"Programming Language : "
            f"{self.programming_language}"
        )


# ==========================================================
#                     UDF FUNCTIONS
# ==========================================================


# ------------------------- UDF 1 -------------------------

def create_person():

    print("\n========== CREATE A PERSON ==========")

    person_id = input("Enter Person ID : ")
    name = input("Enter Name : ")
    age = int(input("Enter Age  : "))
    salary = float(input("Enter Salary : "))

    person = {
        "Person ID": person_id,
        "Name": name,
        "Age": age,
        "Salary": salary
    }

    print("\nPerson Created Successfully!")
    print("Person ID :", person["Person ID"])
    print("Name      :", person["Name"])
    print("Age       :", person["Age"])
    print("Salary    :", person["Salary"])

    input("\nPress Enter To Continue...")

    return person


# ------------------------- UDF 2 -------------------------

def create_employee():

    print("\n========== CREATE AN EMPLOYEE ==========")

    employee_id = input("Enter Employee ID : ")
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    salary = float(input("Enter Salary : "))

    # Using Class Method
    employee = Employee.from_values(
        employee_id,
        name,
        age,
        salary
    )

    print("\nEmployee Created Successfully!")

    employee.display()

    # Demonstrating __str__()
    print("\nUsing __str__() Method:")
    print(employee)

    input("\nPress Enter To Continue...")

    return employee


# ------------------------- UDF 3 -------------------------

def create_manager():

    print("\n========== CREATE A MANAGER ==========")

    employee_id = input("Enter Employee ID : ")
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    salary = float(input("Enter Salary : "))
    department = input("Enter Department : ")

    manager = Manager(
        employee_id,
        name,
        age,
        salary,
        department
    )

    print("\nManager Created Successfully!")

    manager.display()

    print("\nUsing inherited __str__() Method:")
    print(manager)

    print("=====================================")

    input("\nPress Enter To Continue...")

    return manager


# ------------------------- UDF 4 -------------------------

def create_developer():

    print("\n========== CREATE A DEVELOPER ==========")

    employee_id = input("Enter Employee ID : ")
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    salary = float(input("Enter Salary : "))
    department = input("Enter Department : ")
    programming_language = input(
        "Enter Programming Language : "
    )

    developer = Developer(
        employee_id,
        name,
        age,
        salary,
        department,
        programming_language
    )

    print("\nDeveloper Created Successfully!")

    developer.display()

    print("\nUsing inherited __str__() Method:")
    print(developer)

    print("=====================================")

    input("\nPress Enter To Continue...")

    return developer


# ------------------------- UDF 5 -------------------------

def show_details(objects):

    print("\n========== SHOW DETAILS ==========")

    if len(objects) == 0:

        print("No records available.")

        input("\nPress Enter To Continue...")

        return

    print("""
Choose Details To Display:

1. Employee
2. Manager
3. Developer
4. Show All Records
""")

    show = input("Enter Your Choice : ")

    match show:

        # ---------------- EMPLOYEE DETAILS ----------------

        case "1":

            found = False

            for obj in objects:

                if type(obj) is Employee:

                    found = True

                    print(
                        "\n========== EMPLOYEE DETAILS =========="
                    )

                    obj.display()

                    print("\n__str__() Output:")
                    print(obj)

                    print("=====================================")

            if not found:

                print(
                    "\nEmployee has not been created yet."
                )

            input("\nPress Enter To Continue...")


        # ---------------- MANAGER DETAILS ----------------

        case "2":

            found = False

            for obj in objects:

                if isinstance(obj, Manager):

                    found = True

                    print(
                        "\n========== MANAGER DETAILS =========="
                    )

                    obj.display()

                    print("\n__str__() Output:")
                    print(obj)

                    print(
                        "\nIs Manager Subclass of Employee?"
                    )

                    print(
                        issubclass(Manager, Employee)
                    )

                    print("=====================================")

            if not found:

                print(
                    "\nManager has not been created yet."
                )

            input("\nPress Enter To Continue...")


        # ---------------- DEVELOPER DETAILS ----------------

        case "3":

            found = False

            for obj in objects:

                if isinstance(obj, Developer):

                    found = True

                    print(
                        "\n========== DEVELOPER DETAILS =========="
                    )

                    obj.display()

                    print("\n__str__() Output:")
                    print(obj)

                    print(
                        "\nIs Developer Subclass of Employee?"
                    )

                    print(
                        issubclass(Developer, Employee)
                    )

                    print("=====================================")

            if not found:

                print(
                    "\nDeveloper has not been created yet."
                )

            input("\nPress Enter To Continue...")


        # ---------------- ALL DETAILS ----------------

        case "4":

            print("\n========== ALL RECORDS ==========")

            for i, obj in enumerate(objects, start=1):

                print(f"\n----- Record {i} -----")

                obj.display()

                print("\n__str__() Output:")
                print(obj)

                if isinstance(obj, Manager):

                    print(
                        "\nIs Manager Subclass of Employee?"
                    )

                    print(
                        issubclass(Manager, Employee)
                    )

                elif isinstance(obj, Developer):

                    print(
                        "\nIs Developer Subclass of Employee?"
                    )

                    print(
                        issubclass(Developer, Employee)
                    )

                print("=====================================")

            input("\nPress Enter To Continue...")


        # ---------------- INVALID CHOICE ----------------

        case _:

            print("\nInvalid Choice!")

            print("Please select a valid option.")

            input("\nPress Enter To Continue...")


# ------------------------- UDF 6 -------------------------

def main_menu():

    records = []

    while True:

        print("\n")
        print("=" * 60)

        print(
            "   PYTHON OOP PROJECT: "
            "EMPLOYEE MANAGEMENT SYSTEM"
        )

        print("=" * 60)

        print("\nChoose an operation:")

        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Exit")

        print("=" * 60)

        try:

            choice = input("Enter your choice : ")

        except:

            print("\nPlease enter a valid number.")

            continue

        match choice:

            # ---------------- CREATE PERSON ----------------

            case "1":

                create_person()


            # ---------------- CREATE EMPLOYEE ----------------

            case "2":

                employee = create_employee()

                records.append(employee)


            # ---------------- CREATE MANAGER ----------------

            case "3":

                manager = create_manager()

                records.append(manager)


            # ---------------- CREATE DEVELOPER ----------------

            case "4":

                developer = create_developer()

                records.append(developer)


            # ---------------- SHOW DETAILS ----------------

            case "5":

                show_details(records)


            # ---------------- EXIT ----------------

            case "6":

                print("=====================================")

                print(
                    "\nThank you for using "
                    "Employee Management System!"
                )

                print("=====================================")

                print("Have a Good Day!!")

                print("=====================================")

                print("Program Exited Successfully.")

                print("=====================================")

                input("\nPress Enter To Continue...")

                break


            # ---------------- INVALID CHOICE ----------------

            case _:

                print("\nInvalid Choice!")

                print("Please select a valid option.")


# ==========================================================
#                     PROGRAM START
# ==========================================================

main_menu()