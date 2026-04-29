from project import *

NormalPatient("Sara", 22, "454323456", "Good", "Female", doctor_assigned="Dr. Ahmed")
EmergencyPatient("Ali", 30, "789654123", "Critical", "Male", priority=1, room_number="ER-2")
VIPPatient("Noor", 15, "123456789", "Stable", "Female", vip_level=2)

def modify_patient(patient, new_age=None, new_phone=None, new_condition=None):
    if new_age is not None:
        patient.age = new_age
    if new_phone is not None:
        patient.phone = new_phone
    if new_condition is not None:
        patient.condition = new_condition
    print("Patient data updated.")

def menu():
    while True:
        print("\n1. Add new patient")
        print("2. Show patient information")
        print("3. Show all patients")
        print("4. Delete patient")
        print("5. Modify patient information")
        print("6. Show patients sorted by age")
        print("7. Filter patients by age group")
        print("8. Patients count by age group")
        print("9. Increase patient age (Yearly Update)")
        print("10. Check if patient state is stable")
        print("11. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("\nSelect patient type:\n1. Normal\n2. Emergency\n3. VIP")
            type_choice = input("Select type (1-3): ")
            name = input("Patient name: ")
            try:
                age = int(input("Age: "))
                gender = input("Gender: ")
                phone = input("Phone: ")
                condition = input("State: ")
                if type_choice == "1":
                    dr = input("Doctor: ")
                    NormalPatient(name, age, phone, condition, gender, dr)
                elif type_choice == "2":
                    pr = int(input("Priority (1-3): "))
                    rm = input("Room: ")
                    EmergencyPatient(name, age, phone, condition, gender, pr, rm)
                elif type_choice == "3":
                    vp = int(input("VIP Level (1-5): "))
                    VIPPatient(name, age, phone, condition, gender, vp)
                print("Patient added successfully.")
            except ValueError:
                print("Invalid numerical input.")

        elif choice == "2":
            name = input("Enter name: ")
            p = Patient.all_patients.get(name)
            if p:
                print(p)
            else:
                print("Not found.")

        elif choice == "3":
            for p in Patient.all_patients.values():
                print(p)

        elif choice == "4":
            name = input("Name to delete: ")
            Patient.delete_patient(name)

        elif choice == "5":
            name = input("Enter name: ")
            p = Patient.all_patients.get(name)
            if p:
                sub = input("Modify: 1.Age 2.Phone 3.Condition: ")
                if sub == "1": modify_patient(p, new_age=int(input("New Age: ")))
                elif sub == "2": modify_patient(p, new_phone=input("New Phone: "))
                elif sub == "3": modify_patient(p, new_condition=input("New Condition: "))

        elif choice == "6":
            for p in sorted(Patient.all_patients.values(), key=lambda x: x.age):
                print(p)

        elif choice == "7":
            groups = {"1": "Child", "2": "Teenager", "3": "Adult", "4": "Senior"}
            g = groups.get(input("1.Child 2.Teen 3.Adult 4.Senior: "))
            if g:
                for p in filter(lambda x: x.age_group == g, Patient.all_patients.values()):
                    print(p)

        elif choice == "8":
            for g in ["Child", "Teenager", "Adult", "Senior"]:
                count = len([p for p in Patient.all_patients.values() if p.age_group == g])
                print(f"{g}: {count}")

        elif choice == "9":
            name = input("Enter name: ")
            p = Patient.all_patients.get(name)
            if p:
                p += 1
                print(f"Age updated. New age: {p.age}")

        elif choice == "10":
            name = input("Enter name: ")
            p = Patient.all_patients.get(name)
            if p:
                if bool(p):
                    print("Patient state is stable.")
                else:
                    print("Patient needs urgent attention.")

        elif choice == "11":
            break

if __name__ == "__main__":
    menu()
