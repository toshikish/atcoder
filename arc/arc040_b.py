N, R = map(int, input().split())
S = list(input())

l = r = -1
for i in range(N):
    if S[i] == 'o':
        continue
    if l == -1:
        l = i
    r = i

if l == -1:
    ans = 0
else:
    ans = max(r - R + 1, 0)
    i = l
    while i < N:
        if S[i] == 'o':
            i += 1
            continue
        ans += 1
        i += R

print(ans)
