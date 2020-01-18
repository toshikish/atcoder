N = int(input())
P = []
for i in range(N):
    Xi, Li = map(int, input().split())
    P.append((Xi + Li, Xi - Li))

P.sort()
ans = 0
t = -1000000000
for p in P:
    if p[1] >= t:
        ans += 1
        t = p[0]
print(ans)
