scores = [10, 20, 30]

scores.insert(2, 25)
print("After insert:", scores)

scores[-1] = 35
print("After modifying last score:", scores)

scores = scores + [40, 50]
print("After concatenation:", scores)
