N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)
for i in range(M):
    cnt[A[i]] += 1
found = [ci == 0 for ci in cnt]
for i in range(N - M):
    cnt[A[i + M]] += 1
    cnt[A[i]] -= 1
    found[A[i]] = found[A[i]] or cnt[A[i]] == 0

print(found.index(True))
