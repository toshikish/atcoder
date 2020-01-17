from functools import reduce

N, M = map(int, input().split())
a = list(map(int, input().split()))


def f(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def gcd(x, y):
    return gcd(y, x % y) if y != 0 else x


nth = [f(ai) for ai in a]
if len(set(nth)) == 1:
    half_a = [ai >> 1 for ai in a]
    L = reduce(lambda x, y: x * y // gcd(x, y), half_a)
    ans = (M - L) // (2 * L) + 1 if M >= L else 0
else:
    ans = 0
print(ans)
