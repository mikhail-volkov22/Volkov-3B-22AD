class Student:
    def __init__(self, name, surname, year, grades=dict()) -> None:
        self.name = name
        self.surname = surname
        self.year = year
        self.grades = grades

    def average_grade(self):
        return sum(self.grades.values())/len(self.grades.values())


man = Student("Андрей", "Попов", 2, {"химия":5, "биоинженерия":4})
print(man.average_grade())