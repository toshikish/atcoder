N = int(input())
a = [int(input()) for i in range(N)]

c = {}
n = 0
for ai in sorted(a):
    if ai not in c:
        c[ai] = n
        n += 1
for ai in a:
    print(c[ai])
