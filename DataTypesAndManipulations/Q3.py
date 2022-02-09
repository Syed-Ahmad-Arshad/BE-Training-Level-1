import json
from collections import Counter
file = open("birthday_data.json", "r")
birthday_data = file.read()
birthday_data = json.loads(birthday_data)
file.close()
month_data = []
for k in birthday_data.values():
    sp = k.split("/")
    month_data.append(sp[1])
res = Counter(month_data)
print(res)

