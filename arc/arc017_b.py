N, K = map(int, input().split())

ans = 0
c = 0
Ap = 0
for i in range(N):
    Ai = int(input())
    if Ai > Ap:
        c += 1
    else:
        ans += max(c - K + 1, 0)
        c = 1
    Ap = Ai
ans += max(c - K + 1, 0)
print(ans)
