class Car:
 def __init__(self, brand, model, year, price):
  self.brand = brand
  self.model = model
  self.year = year
  self.price = price

 def info(self):
  print(f"{self.brand}-{self.model}, {self.year} год, {self.price} рублей")
auto = Car("Mercedes-Benz", "STS", 2457, 3388956)
auto.info()