import re

class AgeBelow16(BaseException):
    error = "Age is below 16."

    def __init__(self, name):
        print(name + " - " + self.error)
class AgeInvalid(BaseException):
    error = "Age is invalid."

    def __init__(self, name):
        print(name + " - " + self.error)

class EmailInvalid(BaseException):
    error = "Email is invalid.."

    def __init__(self, name):
        print(name + " - " + self.error)

class DuplicateRecord(BaseException):
    error = "Record already exists."

    def __init__(self, name):
        print(name + " - " + self.error)

def email_is_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    return False

list = [
    ("Phoebs", "phoebe@gmail.com", 23),
    ("Rachel", "rachelgreen@gmail.com", 20),
    ("Joey", "joey.com", 16),
    ("Raptor", "raptor@fighter.com", 11),
    ("Neil Bohr", "rachelgreen@gmail.com", 23),
    ("Rachel", "rachelagain@gmail.com", 23)
]
valid_users = dict()

for data in list:
    try:
        if data[2] < 0:
            raise AgeInvalid(data[0])
        if not email_is_valid(data[1]):
            raise EmailInvalid(data[0])
        if data[2] < 16:
            raise AgeBelow16(data[0])
        if valid_users.get(data[0]):
            raise DuplicateRecord(data[0])
    except AgeInvalid:
        continue
    except EmailInvalid:
        continue
    except AgeBelow16:
        continue
    except DuplicateRecord:
        continue
    valid_users[data[0]] = data[1]

print("\n\nThe valid users are: ")
for users in valid_users.keys():
    print(users)