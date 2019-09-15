S = input()

ans = True
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] not in ['R', 'U', 'D']:
            ans = False
            break
    else:
        if S[i] not in ['L', 'U', 'D']:
            ans = False
            break
print('Yes' if ans else 'No')
