months = ("Jan", "Feb", "Mar")

try:
    months[1] = "April"
except TypeError as e:
    print("Error:", e)

fruits = ["apple", "banana", "mango"]
fruits[1] = "kiwi"
print("Updated fruits:", fruits)
