x = int(input())

q = x // 11
r = x % 11
if r == 0:
    s = 0
elif r <= 6:
    s = 1
else:
    s = 2
print(q * 2 + s)
