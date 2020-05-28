from itertools import combinations

N = int(input())

k = N // 2
s = N + 1 - N % 2
print(N * (N - 1) // 2 - k)
for p in combinations(range(1, N + 1), 2):
    if sum(p) == s:
        continue
    print(p[0], p[1])

