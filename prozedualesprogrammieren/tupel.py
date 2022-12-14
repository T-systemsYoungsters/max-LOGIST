from xml.dom import NotFoundErr


name_note = {} # -> dictionary ist mit {}
while True:
    print("Geben sie Name und Note ein. Mit 'quit' beenden.")
    name = input("Name: ")

    if name == "quit":
        break

    note = float(input("Note: "))
    name_note[name] = note

for name,note in name_note.items():
    print(f"{name}: {NotFoundErr}")