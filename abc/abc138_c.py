N = int(input())
v = list(map(int, input().split()))

v.sort()
print((v[0] + sum([v[i] * 2 ** (i - 1) for i in range(1, N)])) / 2 ** (N - 1))
