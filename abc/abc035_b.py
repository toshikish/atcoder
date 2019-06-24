from collections import defaultdict

S = list(input())
T = int(input())

commands = defaultdict(int)
for s in S:
    commands[s] += 1
x = commands['L'] - commands['R']
y = commands['U'] - commands['D']
dm = abs(x) + abs(y)
q = commands['?']

if T == 1:
    ans = dm + q
else:
    if dm >= q:
        ans = dm - q
    else:
        ans = (q - dm) % 2
print(ans)
