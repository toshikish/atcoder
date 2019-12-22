A, B = map(int, input().split())


def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    return gcd(n, m % n)


print(A * B // gcd(A, B))
