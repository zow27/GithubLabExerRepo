class SavingsAccount:
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"

    # 🔽 Add this method so SavingsAccount objects can be sorted
    def __lt__(self, other):
        return self.name < other.name
