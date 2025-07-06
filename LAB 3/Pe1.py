class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Alice")

    print("student1 == student2:", student1 == student2)  # False
    print("student1 == student3:", student1 == student3)  # True
    print("student1 < student2:", student1 < student2)    # True (alphabetical)
    print("student2 < student1:", student2 < student1)    # False
    print("student1 >= student2:", student1 >= student2)  # False
    print("student2 >= student1:", student2 >= student1)  # True
    print("student1 >= student3:", student1 >= student3)  # True

if __name__ == "__main__":
    main()
