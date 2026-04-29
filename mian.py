

stack=[]
MAX_SIZE=5
def clear_stack():
    stack.clear()

def push_stack(item):
    if len(stack)>=MAX_SIZE:
        print("stack is full")
    else:
        stack.append(item)
        print(f"Item{item} append to stack")
def pop_stack():
    if len (stack) == 0:
        print("stack is empty")
        return None
    else:
        item=stack.pop()
        print(f" Item {item} pop from stack")
        return item
def display_stack():
    if len(stack) ==0:
        print("stack is empty")

    else:
        print("stack element (top to bottom):")
        for item in reversed(stack):
            print(item)


push_stack(10)
push_stack(20)
push_stack(30)
display_stack()
pop_stack()
display_stack()
push_stack(50)
push_stack(60)
push_stack(70)
display_stack()
push_stack(80)
display_stack()






def menu():
    while True:
        print("\n--- Patient Management System ---")
        print("1. Add patient")
        print("2. Show patient")
        print("3. Delete patient")
        print("4. Show all patients")
        print("5. Modify patient")
        print("6. Sort patients")
        print("7. Filter by age group")
        print("8. Count patients by age group")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == "5":
            name = input("Patient name to modify: ")
            patient = Patient.all_patients.get(name)

            if patient:
                print("\nModify options:")
                print("1. New name")
                print("2. New phone")
                print("3. New condition")

                sub = input("Choose: ")

                if sub == "1":
                    new_name = input("New name: ")
                    modify_patient(patient, new_name=new_name)

                elif sub == "2":
                    new_phone = input("New phone: ")
                    modify_patient(patient, new_phone=new_phone)

                elif sub == "3":
                    new_condition = input("New condition: ")
                    modify_patient(patient, new_condition=new_condition)

                else:
                    print("Invalid choice.")
            else:
                print("This patient does not exist.")

        elif choice == "6":
            sorted_patients = sorted(Patient.all_patients.values())
            for patient in sorted_patients:
                print(patient.show_info())
                print("Age group:", patient.age_group)

        elif choice == "7":
            print("\nSelect age group to filter:")
            print("1. Child")
            print("2. Teenager")
            print("3. Adult")
            print("4. Senior")

            group_choice = input("Choose: ")

            groups = {
                "1": "Child",
                "2": "Teenager",
                "3": "Adult",
                "4": "Senior"
            }

            selected_group = groups.get(group_choice)

            if selected_group:
                filtered = list(filter(
                    lambda p: p.age_group == selected_group,
                    Patient.all_patients.values()
                ))

                for patient in filtered:
                    print(patient.show_info())
                    print("Age group:", patient.age_group)
            else:
                print("Invalid choice.")

        elif choice == "8":
            groups = ["Child", "Teenager", "Adult", "Senior"]
            print("\nPatients count by age group:")

            for g in groups:
                count = len(list(filter(
                    lambda p: p.age_group == g,
                    Patient.all_patients.values()
                )))
                print(g, ":", count)

        elif choice == "9":
            print("System closed.")
            break

        else:
            print("Invalid choice.")
















