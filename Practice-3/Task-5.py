class BankAccount:
 def __init__(self, owner, profile, balance):
  self.owner = owner
  self.profile = profile
  self.balance = balance

 def deposit(self, amount):
  self.balance += amount

 def back(self, amount):
  if self.balance >= amount:
   self.balance -= amount
  else:
   print("Нет средств")

 def __str__(self):
  return f"Счет № {self.profile} на имя {self.owner}. Баланс: {self.balance}"
profile1 = BankAccount("Волков Михаил", "873987445", 1200)
print(profile1)
profile1.deposit(40)
print(profile1)
profile1.back(50)
print(profile1)
profile1.back(10)
print(profile1)