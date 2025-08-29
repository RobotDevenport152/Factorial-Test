# Base class
class Person:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def display_info(self):
        return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.ID}"


# Student inherits from Person
class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    def display_info(self):
        return super().display_info() + f", Academic Record: {self.academic_record}"


# Academic inherits from Person
class Academic(Person):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        return super().display_info() + f", Tax Code: {self.tax_code}, Salary: {self.salary}"


# Staff inherits from Person
class Staff(Person):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        return super().display_info() + f", Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}