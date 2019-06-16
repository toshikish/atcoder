N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
ans = 1 if D <= X else 0
for i in range(N):
    D += L[i]
    if D <= X:
        ans += 1
print(ans)
