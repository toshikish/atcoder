import sys
sys.setrecursionlimit(300000)

Q = int(input())
N = 2 ** 20

A = [-1] * N
nx = list(range(1, N)) + [0]


def update(h, x):
    if A[h] == -1:
        A[h] = x
        return h
    nx[h] = update(nx[h], x)
    return nx[h]


for _ in range(Q):
    ti, xi = map(int, input().split())
    if ti == 1:
        update(xi % N, xi)
    else:
        print(A[xi % N])
