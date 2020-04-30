from collections import Counter

H, W = map(int, input().split())
a = ''
for i in range(H):
    a += input()

c = Counter(a)
n = c.values()
T = [0,
     sum(ni // 4 for ni in n),
     sum((ni % 4) // 2 for ni in n),
     sum(ni % 2 for ni in n)]
E = [(H // 2) * (W // 2),
     (H // 2) * (W % 2) + (H % 2) * (W // 2),
     (H % 2) * (W % 2)]

ans = True
for i in range(3):
    T[i + 1] += T[i] * 2
    T[i + 1] -= E[i]
    if T[i + 1] < 0:
        ans = False
        break
print('Yes' if ans else 'No')
