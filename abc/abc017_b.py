S = input()

ans = True
while S != '':
    if S[-2:] == 'ch':
        S = S[:-2]
    elif S[-1:] in ['o', 'k', 'u']:
        S = S[:-1]
    else:
        ans = False
        break
print('YES' if ans else 'NO')
