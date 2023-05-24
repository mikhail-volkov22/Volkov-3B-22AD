class Book:
 def __init__(self, title, author, year, genre):
  self.title = title
  self.author = author
  self.year = year
  self.genre = genre

 def info(self):
  print(f"{self.title}, {self.author} ({self.year}), {self.genre}")
book = Book("Война и мир", "Лев Николаевич Толстой", 1865, "роман-эпопея")
book.info()