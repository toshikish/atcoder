N = input().rstrip('0')

ans = True
L = len(N)
for i in range(L // 2):
    if N[i] != N[L - 1 - i]:
        ans = False
        break
print('Yes' if ans else 'No')
