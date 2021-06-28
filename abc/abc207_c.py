N = int(input())
S = []
for _ in range(N):
    ti, li, ri = map(int, input().split())
    li *= 2
    ri *= 2
    if ti == 2 or ti == 4:
        ri -= 1
    if ti == 3 or ti == 4:
        li += 1
    S.append((li, ri))

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        Si, Sj = S[i], S[j]
        if Si[0] <= Sj[0] <= Si[1] or Si[0] <= Sj[1] <= Si[1] or Sj[0] <= Si[0] <= Sj[1]:
            ans += 1
print(ans)
