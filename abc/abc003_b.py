S = input()
T = input()

win = True
for i in range(len(S)):
    if S[i] == T[i] == '@':
        continue
    elif S[i] == '@':
        if T[i] not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:
            win = False
            break
    elif T[i] == '@':
        if S[i] not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:
            win = False
            break
    else:
        if S[i] != T[i]:
            win = False
            break
print('You can win' if win else 'You will lose')
