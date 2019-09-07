N, K = map(int, input().split())
S = input()

ans = 0
c = 0
for i in range(N):
    if S[i] == 'L':
        if i > 0 and S[i - 1] == 'L':
            ans += 1
    elif S[i] == 'R':
        if i < N - 1 and S[i + 1] == 'R':
            ans += 1
    if i < N - 1 and S[i] != S[i + 1]:
        c += 1

if c % 2 == 0:
    max_K = c // 2
    ans += min(K, max_K) * 2
else:
    max_K = (c - 1) // 2
    ans += min(K, max_K) * 2
    if K > max_K:
        ans += 1
print(ans)
