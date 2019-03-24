S = input()

len_S = len(S)
ans = 0
current = 0
for i in range(len_S):
    if S[i] in 'ACGT':
        current += 1
        ans = max(ans, current)
    else:
        current = 0
print(ans)
