from collections import defaultdict
N, M = map(int, input().split())
D = defaultdict(int)
for i in range(N):
    A, B = map(int, input().split())
    D[A] += B

ans = 0
for i in sorted(D.keys()):
    if M > D[i]:
        ans += i * D[i]
        M -= D[i]
    else:
        ans += i * M
        M -= M
    if M <= 0:
        break
print(ans)
