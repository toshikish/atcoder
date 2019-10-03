n = int(input())
a = list(map(int, input().split()))

t = [0]
for i in range(1, 10):
    if i % 2 == 1 and i % 3 != 2:
        t.append(0)
    else:
        t.append(t[-1] + 1)

print(sum([t[ai] for ai in a]))
