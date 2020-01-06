N, M = map(int, input().split())
Q = [tuple(map(int, input().split())) for i in range(M)]

Q.sort(key=lambda x: x[1])
ans = 0
prev = 0
for ai, bi in Q:
    if prev < ai:
        ans += 1
        prev = bi - 1
print(ans)
