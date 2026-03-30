import json
import os


class JsonFile:
    def __init__(self, filename) -> None:
        script_path = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(script_path, filename)
        if not os.path.exists(self.filepath):
            self.write([])

    def write(self, data):
        with open(self.filepath, "w") as file:
            json.dump(data, file)

    def read(self):
        with open(self.filepath, "r") as file:
            return json.load(file)

    def append(self, data):
        stuff = self.read()
        stuff.append(data)
        self.write(stuff)

    def update(self, number, change):
        data = self.read()
        for i in data:
            if i["number"] == number:
                i["done"] = change
        self.write(data)

    def size(self):
        data = self.read()
        return len(data)


print("""
    WELCOME TO MY TODO LIST!
    """)

want = True

db = JsonFile("tasks.json")

while want:
    print("What would you like to do?")
    print("""
       1. View tasks
       2. Add tasks
       3. Change status""")
    choice = int(input("Enter choice (1, 2, 3): "))

    if choice == 1:
        data = db.read()
        print(data)
    elif choice == 2:
        task = input("Enter task: ")
        db.append({"task": task, "done": False, "number": db.size() + 1})

    elif choice == 3:
        print(db.read())
        number = int(input("Which one to change? : "))
        done = input("Done? (y/n): ")
        if done == "y":
            status = True
        else:
            status = False

        db.update(number, status)

    else:
        print("Bye!")
        want = False
