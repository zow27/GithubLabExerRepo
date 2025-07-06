import random

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

    def display_info(self):
        print(f"Name: {self.name}")

def main():
    # Create a list of students
    students = [
        Student("Zara"),
        Student("Alice"),
        Student("Charlie"),
        Student("Bob"),
        Student("Eve")
    ]

    print("Original list:")
    for student in students:
        student.display_info()

    # Shuffle the list
    random.shuffle(students)

    print("\nShuffled list:")
    for student in students:
        student.display_info()

    # Sort the list
    students.sort()

    print("\nSorted list:")
    for student in students:
        student.display_info()

if __name__ == "__main__":
    main()
