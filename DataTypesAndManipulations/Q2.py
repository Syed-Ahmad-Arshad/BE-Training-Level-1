import json
file = open("birthday_data.json", "r")
birthday_data = file.read()
birthday_data = json.loads(birthday_data)
file.close()
print("Welcome to the birthday dictionary. We know the birthdays of:")
for k in birthday_data.keys():
    print(k)
name = input("Who's birthday do you want to look up?")
if birthday_data.get(str(name)):
    print(name, "has birthday on", birthday_data[str(name)])
else:
    print("This person doesn't exist.")
choice = input("Do you want to add a record of your choice?? (y/n) ")
if choice == 'y':
    name = input("Add the name you want to add DOB of: ")
    dob = input("Let us know the DOB of ")
    birthday_data[name] = dob
    file = open("birthday_data.json", "w")
    birthday_data = json.dumps(birthday_data)
    print("LOL: ", birthday_data)
    file.write(birthday_data)
    file.close()
