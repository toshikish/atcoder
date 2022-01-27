import sys

sys.setrecursionlimit(100000)

N, X = map(int, input().split())
a = []
for _ in range(N):
    ai = list(map(int, input().split()))
    a.append(ai[1:])


def dfs(i, p):
    if i == N:
        return 1 if p == X else 0
    ans = 0
    for aij in a[i]:
        np = p * aij
        if np <= X:
            ans += dfs(i + 1, np)
    return ans


print(dfs(0, 1))
