A, B = map(int, input().split())


def S(x):
    a = 0
    while x > 0:
        a += x % 10
        x //= 10
    return a


print(max(S(A), S(B)))
