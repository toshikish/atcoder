S = input()
T = input()

def rotatable(s, t):
    for i in range(len(s)):
        s = s[-1] + s[0:-1]
        if s == t:
            return True
    return False

if rotatable(S, T):
    print('Yes')
else:
    print('No')
