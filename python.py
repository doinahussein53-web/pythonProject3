


class Patient:
    all_patients = []

    def __init__(self, name, disease, age, city):
        self.name = name
        self.disease = disease
        self.city = city
        self.set_age(age)
        Patient.all_patients.append(self)

    def set_age(self, age):
        if 1 <= age <= 120:
            self.age = age
        else:
            print(" age must be between 1 and 120")

    def print_info(self):
        if self.city == "Basra":
            print(f"Name: {self.name}, Disease: {self.disease}, Age: {self.age}, City: {self.city}")

    @classmethod
    def count_seniors(cls, city):
        count = 0
        for p in cls.all_patients:
            if p.city == city:
                count += 1
        print(f"Number of patients in {city}: {count}")


# إنشاء 4 مرضى
p1 = Patient("Ali", "Flu", 25, "Basra")
p2 = Patient("Sara", "Cold", 30, "Baghdad")
p3 = Patient("Omar", "Asthma", 50, "Basra")
p4 = Patient("Noor", "Fever", 19, "Mosul")

print("Patients from Basra:")
p1.print_info()
p2.print_info()
p3.print_info()
p4.print_info()

Patient.count_seniors("Basra")
Patient.count_seniors("Baghdad")
Patient.count_seniors("Mosul")


class Student:
    def __init__(self, name, address, grades):
        self.name = name
        self.address = address
        self.__grades = grades   # خاص (private)

    # دالة لإرجاع الدرجة
    def get_grades(self):
        return self.__grades

    # دالة لتحديد النجاح أو الرسوب
    def check_pass_fail(self):
        if self.__grades >= 50:
            print(f"{self.name} is Passed ✅")
        else:
            print(f"{self.name} is Failed ❌")


# إنشاء طلاب
s1 = Student("Ali", "Basra", 70)
s2 = Student("Sara", "Baghdad", 40)

# طباعة النتائج
print("Grades of students:")
print(f"{s1.name}: {s1.get_grades()}")
print(f"{s2.name}: {s2.get_grades()}")

# التحقق من النجاح أو الرسوب
s1.check_pass_fail()
s2.check_pass_fail()

class BankAccount:
    def __init__(self, name, address, balance):
        self.name = name
        self.address = address
        self.__balance = balance   # خاص (private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance = {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance = {self.__balance}")
        else:
            print("Not enough balance or invalid amount!")

    def get_balance(self):
        print(f"Current balance: {self.__balance}")
acc1= BankAccount("donia", "basra",100)
acc1.get_balance()
acc1.deposit(50)
acc1.withdraw(30)
acc1.get_balance()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # الراتب خاص (private)

    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"raise {amount}. New salary = {self.__salary}")
        else:
            print("Invalid raise amount!")

    def get_salary(self):
        print(f" current salary is: {self.__salary}")
emp1 = Employee("Donia", 800)
emp1.get_salary()       # يعرض الراتب الحالي
emp1.give_raise(200)    # زيادة الراتب
emp1.get_salary()       # عرض الراتب الجديد

class Robot:
    def __init__(self):
        self.__powered_on = False  # بالبداية مطفأ

    def power_on(self):
        self.__powered_on = True
        print("Robot is now ON.")

    def power_off(self):
        self.__powered_on = False
        print("Robot is now OFF.")

    def is_powered_on(self):
        return self.__powered_on
r1 = Robot()         # صنع روبوت
r1.power_on()        # شغّله
print(r1.is_powered_on())  # نعرف حالته
r1.power_off()       # نطفيه


class Employee:
    def __init__(self, name):
        self.name = name

        self.__attendance = 0  # عداد الحضور خاص

    def mark_attendance(self):
        self.__attendance += 1
        print(f"{self.name}'s attendance marked. Total: {self.__attendance}")

    def get_attendance(self):
        return self.__attendance
emp1 = Employee("Ali")
emp1.mark_attendance()
print("Attendance count:", emp1.get_attendance())























class Robot:
    def __int__(self):
        self.__powered_on=False
    def power_on(self):
        self.__powered_on=True
        print("Robot is no new")
    def power_off(self):
        self.__powered_on=False
        print(("Robot is new off."))
    

    def is powered_no(self):









