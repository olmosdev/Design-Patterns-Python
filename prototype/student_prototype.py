from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Student(Prototype):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        school_id: str,        
        grade: int,
        school_email: str,
        school_phone: str,
        school_address: str
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.school_id = school_id
        self.grade = grade
        self.school_email = school_email
        self.school_phone = school_phone
        self.school_address = school_address

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
            f"School ID: {self.school_id}, Grade: {self.grade}, "
            f"School Email: {self.school_email}, School Phone: {self.school_phone}, School Address: {self.school_address}"
        )

student = Student("Prototype Student", 20, "Male", "S12345", 3, "prototype@school.edu", "123-456-7890", "123 School St, City, State")

juan = student.clone()
juan.name = "Juan"

pedro = student.clone()
pedro.name = "Pedro"

print(student)
print(juan)
print(pedro)

