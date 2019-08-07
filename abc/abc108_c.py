N, K = map(int, input().split())


def f(x): return x + x * (x - 1) * 3 + x * (x - 1) * (x - 2)


if K % 2 == 0:
    a = N // K
    b = N // (K // 2) - a
    ans = f(a) + f(b)
else:
    ans = f((2 * N) // (K * 2))
print(ans)
