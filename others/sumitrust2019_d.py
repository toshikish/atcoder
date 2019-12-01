from collections import defaultdict

N = int(input())
S = input()

dp = defaultdict(int)
d1 = {S[0], S[1], S[2]}
d2 = {S[0:2], S[1:3], S[0] + S[2]}
pin = {S[0:3]}
for i in range(3, N):
    s = S[i]
    for d in d2:
        pin.add(d + s)
    for d in d1:
        d2.add(d + s)
    d1.add(s)
print(len(pin))
