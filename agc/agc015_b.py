S = input()

N = len(S)
ans = 0
for i in range(N):
    upper = N - i - 1
    lower = i
    if S[i] == 'U':
        ans += upper + lower * 2
    else:
        ans += lower + upper * 2
print(ans)
