from bank import Bank
from savingsaccount import SavingsAccount

b = Bank()
b.add_account(SavingsAccount("Zara", "1111", 1000))
b.add_account(SavingsAccount("Alice", "2222", 1500))
b.add_account(SavingsAccount("Charlie", "3333", 1200))

print(b)
