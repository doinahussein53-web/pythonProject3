class Patient:
    all_patients = {}
    def __init__(self, name, age, phone, condition):
        self.name = name
        self.age = age
        self.phone = phone
        self.condition = condition
        Patient.all_patients[name] = self

    def show_info(self):
        return f"""
    patient name: {self.name}
    age: {self.age}
    phone number: {self.phone}
    state: {self.condition}
    --------------------"""

    @classmethod
    def show_all(cls):
        for patient in cls.all_patients.values():
            print(patient.show_info())