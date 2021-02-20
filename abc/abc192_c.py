N, K = map(int, input().split())


def g1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))


def g2(x):
    return int(''.join(sorted(list(str(x)))))


def f(x):
    return g1(x) - g2(x)


a = N
for i in range(K):
    a = f(a)
print(a)
