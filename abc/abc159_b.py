S = input()

N = len(S)
k = (N - 1) // 2
ans = True
for i in range(k // 2 + 1):
    if S[i] == S[k - 1 - i] == S[k + 1 + i] == S[2 * k - i]:
        continue
    ans = False
    break
if N == 3 and S[0] != S[2]:
    ans = False
print('Yes' if ans else 'No')
