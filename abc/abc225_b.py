N = int(input())
c = [0] * N
for _ in range(N - 1):
    ai, bi = map(lambda s: int(s) - 1, input().split())
    c[ai] += 1
    c[bi] += 1

print('Yes' if max(c) == N - 1 else 'No')
