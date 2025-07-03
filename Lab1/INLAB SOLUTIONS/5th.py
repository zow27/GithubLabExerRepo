def safe_integer_input(prompt):
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Error in number format:", s)

if __name__ == "__main__":
    age = safe_integer_input("Enter your age: ")
    print("Your age is", age)
