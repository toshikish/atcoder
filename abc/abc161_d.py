K = int(input())

F = {}
for i in range(10):
    F[(1, i)] = 1


def f(n, d):
    if (n, d) in F:
        return F[(n, d)]
    nf = 0
    for i in [d - 1, d, d + 1]:
        if 0 <= i <= 9:
            nf += f(n - 1, i)
    F[(n, d)] = nf
    return nf


k = 0
p = (1, 0)
for i in range(1, 11):
    for j in range(1, 10):
        fij = f(i, j)
        if k + fij >= K:
            p = (i, j)
            break
        k += fij
        p = (i, j)
    else:
        continue
    break


def g(n, d, index):
    if n == 1:
        return str(d)
    total = 0
    for i in [d - 1, d, d + 1]:
        if not 0 <= i <= 9:
            continue
        if total + f(n - 1, i) >= index:
            break
        total += f(n - 1, i)
    return str(d) + g(n - 1, i, index - total)


print(g(p[0], p[1], K - k))
