N = int(input())
A = list(map(int, input().split()))


def f(x):
    return sum([Ai % x == 0 for Ai in A])


M = 0
ans = 0
for i in range(2, 1001):
    g = f(i)
    if g > M:
        M = g
        ans = i

print(ans)
