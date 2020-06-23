A, B = map(int, input().split())


def f(x): return x // 4 - x // 100 + x // 400


print(f(B) - f(A - 1))
