N = int(input())
A = list(map(int, input().split()))

ans = 0
m = 0
for Ai in A:
    if m <= Ai:
        m = Ai
    else:
        ans += m - Ai
print(ans)
