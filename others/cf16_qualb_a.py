S = input()

A = 'CODEFESTIVAL2016'
ans = 0
for i in range(16):
    if S[i] != A[i]:
        ans += 1
print(ans)
