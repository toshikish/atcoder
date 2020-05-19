s = input()

S = []
N = len(s)
i = 0
while i < N:
    if i < N - 1 and s[i:i + 2] == 'BC':
        S.append('D')
        i += 2
    else:
        S.append(s[i])
        i += 1

ans = 0
c = 0
for l in S:
    if l == 'A':
        c += 1
    elif l == 'D':
        ans += c
    else:
        c = 0
print(ans)
