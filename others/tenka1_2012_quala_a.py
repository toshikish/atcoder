n = int(input())

c = 1
a = 0
for i in range(n):
    t = c
    c = a
    a += t
print(c + a)
