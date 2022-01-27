from collections import defaultdict

N, Q = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(list)
for i in range(N):
    d[a[i]].append(i + 1)

for _ in range(Q):
    xi, ki = map(int, input().split())
    print(-1 if len(d[xi]) < ki else d[xi][ki - 1])
