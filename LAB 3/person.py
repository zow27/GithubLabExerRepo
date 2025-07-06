class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"{self.name} {self.age} {self.gender}")

person1 = Person("Alice", 30, "Female")
person2 = Person("Bob", 25, "Male")
person3 = Person("Charlie", 40, "Non-binary")

for person in [person1, person2, person3]:
    person.display_info()
