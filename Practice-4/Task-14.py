class Schoolkid:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(f"{self.name} учится в {self.grade} классе.")

student = Schoolkid("Дима", 8)

student.study()