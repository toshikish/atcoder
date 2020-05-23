S = input()

N = len(S)
ans = 0
c = 0
i = 0
while i < N - 1:
    if S[i:i+2] == '25':
        c += 1
        i += 2
    else:
        ans += c * (c + 1) // 2
        c = 0
        i += 1
ans += c * (c + 1) // 2
print(ans)
