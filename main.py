from project import *
NormalPatient("sara", 22, "454323456", "good")
EmergencyPatient("ali", 30, "789654123", "critical", priority=1)
NormalPatient("noor", 25, "123456789", "stable")


def menu():
    while True:
        print("\n1. Add new patient")
        print("2. Show patient information")
        print("3. Show all patients")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("\n1. Normal patient")
            print("2. Emergency patient")
            type_choice = input("Select type: ")

            name = input("Patient name: ")
            age = int(input("Age: "))
            phone = input("Phone number: ")
            condition = input("State: ")

            if type_choice == "1":
                NormalPatient(name, age, phone, condition)
                print("Normal patient added.")
            elif type_choice == "2":
                priority = int(input("Priority (1-3): "))
                EmergencyPatient(name, age, phone, condition, priority)
                print("Emergency patient added.")
            else:
                print("Invalid type selection.")

        elif choice == "2":
            name_to_show = input("Enter patient name: ")
            if name_to_show in Patient.all_patients:
                print(Patient.all_patients[name_to_show].show_info())
            else:
                print("This patient does not exist.")

        elif choice == "3":
            for patient in Patient.all_patients.values():
                print(patient.show_info())

        elif choice == "4":
            print("System closed.")
            break

        else:
            print("Invalid choice, try again.")


menu()
