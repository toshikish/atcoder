S = input()
T = input()

ans = S == T
for i in range(len(S) - 1):
    s = list(S)
    s[i], s[i + 1] = s[i + 1], s[i]
    if ''.join(s) == T:
        ans = True
        break
print('Yes' if ans else 'No')
