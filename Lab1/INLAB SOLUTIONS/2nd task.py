class Counter:
    instances = 0

    def __init__(self):
        Counter.instances += 1
        self.value = 0

    def reset(self):
        self.value = 0

    def increment(self, amount=1):
        self.value += amount

    def decrement(self, amount=1):
        self.value -= amount

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, Counter) and self.value == other.value
