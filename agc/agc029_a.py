S = input()

ans = 0
n = 0
for i in range(len(S)):
    if S[i] == 'W':
        ans += i - n
        n += 1
print(ans)
