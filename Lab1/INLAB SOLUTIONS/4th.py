import pickle

items = [60, "A string object", 1977]
with open("items.dat", "wb") as f:
    pickle.dump(items, f)

with open("items.dat", "rb") as f:
    loaded = pickle.load(f)

print(loaded)
