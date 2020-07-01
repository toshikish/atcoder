A = int(input())

finv = {}
f = 0
k = 10
while f <= 10 ** 16:
    f = 0
    l = len(str(k))
    for i in range(l):
        f += (k // 10 ** (l - i - 1) % 10) * (k ** (l - i - 1))
    finv[f] = k
    k += 1
print(finv[A] if A in finv else -1)
