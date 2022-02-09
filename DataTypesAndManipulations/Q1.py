birthday_data = {
    "Harry Potter": "10 / 10 / 1999",
    "Phoebe Buffay": "11 / 12 / 1995",
    "Chanendler Bong": "07 / 07/ 1997",
    "Mister Tribbiani": "01 / 01 / 2001"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for k in birthday_data.keys():
    print(k)
name = input("Who's birthday do you want to look up?")
if birthday_data.get(str(name)):
    print(name, "has birthday on", birthday_data[str(name)])
else:
    print("This person doesn't exist.")