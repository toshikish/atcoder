S = input()

def isLowerWithoutAC(s):
    l = list(s)
    l.remove('A')
    l.remove('C')
    return ''.join(l).islower()

if S[0] == 'A' and S[2:-1].count('C') == 1 and isLowerWithoutAC(S):
    print('AC')
else:
    print('WA')
