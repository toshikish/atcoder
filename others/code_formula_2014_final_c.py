import re

S = input()

result = re.findall('@([a-z]+)', S)
users = sorted(set(result))
for user in users:
    print(user)
