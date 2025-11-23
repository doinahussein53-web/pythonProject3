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

class NormalPatient(Patient):
    def show_info(self):
        return f"normal Patient" + super().show_info()


class EmergencyPatient(Patient):
    def __init__(self,name,age,phone,condition,priority ):
        super().__init__(name,age,phone,condition)
        self.priority= priority
    def show_info(self):
        return f"EmergencyPatient(priority{self.priority}):"+super().show_info()