
class Student:
    def __init__(self, name, surname, age, speciality) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.speciality = speciality

    def info(self):
        print(f"{self.name} {self.surname}, {self.age} лет, {self.speciality}")


man = Student("Андрей", "Попов", 18, "юрист")
man.info()