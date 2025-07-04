contacts = {"Alice": "555-1234", "Bob": "555-9876"}

print("Charlie's number:", contacts.get("Charlie", "Not found"))

contacts["Charlie"] = "555-4567"
print("After adding Charlie:", contacts)

contacts.pop("Bob")
print("After removing Bob:", contacts)
