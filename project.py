from dataclasses import dataclass
from abc import ABC, abstractmethod

class IPatient(ABC):
    @abstractmethod
    def show_info(self):
        pass

class Patient(IPatient):
    all_patients = {}

    def __init__(self, name, age, phone, condition, gender):
        self._name = name
        self._age = age
        self._phone = phone
        self._condition = condition
        self._gender = gender
        Patient.all_patients[name] = self

    @property
    def name(self): return self._name
    @property
    def age(self): return self._age
    @property
    def phone(self): return self._phone
    @property
    def condition(self): return self._condition
    @property
    def gender(self): return self._gender

    @condition.setter
    def condition(self, value): self._condition = value
    @age.setter
    def age(self, value): self._age = value
    @phone.setter
    def phone(self, value): self._phone = value

    @abstractmethod
    def show_info(self):
        pass

    def __str__(self):
        return self.show_info()

    def __gt__(self, other):
        if isinstance(other, Patient):
            return self._age > other._age
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Patient):
            return self._age <= other._age
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Patient):
            return self._age >= other._age
        return NotImplemented

    def __bool__(self):
        return self._condition.lower() in ["good", "stable"]

    def __len__(self):
        return self._age

    def __iadd__(self, years):
        if isinstance(years, int):
            self._age += years
            return self
        return NotImplemented

    def __getitem__(self, key):
        if key == "name": return self._name
        if key == "age": return self._age
        if key == "condition": return self._condition
        raise KeyError(f"Key {key} not found")

    @property
    def age_group(self):
        if self._age < 13: return "Child"
        elif self._age < 20: return "Teenager"
        elif self._age < 60: return "Adult"
        else: return "Senior"

    @classmethod
    def delete_patient(cls, name):
        if name in cls.all_patients:
            del cls.all_patients[name]
            print(f"Patient {name} deleted.")
        else:
            print("This patient does not exist.")

class NormalPatient(Patient):
    def __init__(self, name, age, phone, condition, gender, doctor_assigned="None"):
        super().__init__(name, age, phone, condition, gender)
        self.doctor_assigned = doctor_assigned

    def __lt__(self, other):
        if isinstance(other, Patient):
            return self.age < other.age
        return NotImplemented

    def show_info(self):
        return (
            f"Normal Patient (Doctor: {self.doctor_assigned})\n"
            f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}\n"
            f"Condition: {self.condition} | Group: {self.age_group}\n"
            "--------------------"
        )

class EmergencyPatient(Patient):
    def __init__(self, name, age, phone, condition, gender, priority, room_number="ER-1"):
        super().__init__(name, age, phone, condition, gender)
        self.priority = priority
        self.room_number = room_number

    def show_info(self):
        return (
            f"EMERGENCY Patient | Priority: {self.priority} | Room: {self.room_number}\n"
            f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}\n"
            f"Condition: {self.condition} | Group: {self.age_group}\n"
            "--------------------"
        )

class VIPPatient(Patient):
    def __init__(self, name, age, phone, condition, gender, vip_level=1):
        super().__init__(name, age, phone, condition, gender)
        self.vip_level = vip_level

    def show_info(self):
        return (
            f"VIP Patient | Level: {self.vip_level}\n"
            f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}\n"
            f"Condition: {self.condition} | Group: {self.age_group}\n"
            "--------------------"
        )
