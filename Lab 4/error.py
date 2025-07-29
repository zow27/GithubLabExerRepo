scores = [10, 20, 30]

try:
    print(scores[10])
except IndexError:
    print("Index out of range! Please use a valid index.")
