from project import Patient

Patient("sara", 22, "454323456", "good")
Patient("ali", 30, "789654123", "critical")
Patient("noor", 25, "123456789", "stable")

def menu():
    while True:
        print("\n1. Add new patient")
        print("2. Show patient information")
        print("3. Show all patients")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Patient name: ")
            age = int(input("Age: "))
            phone = input("Phone number: ")
            condition = input("State: ")
            Patient(name, age, phone, condition)
            print("Patient added successfully")

        elif choice == "2":
            name_to_show = input("Enter patient name to display information: ")

            if name_to_show in Patient.all_patients:
                print(Patient.all_patients[name_to_show].show_info())
            else:
                print("This patient does not exist.")

        elif choice == "3":
            print(Patient.show_all())

        elif choice == "4":
            print("System closed.")
            break

        else:
            print("Invalid choice, try again.")

menu()