S = input()

T = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
L = len(S)
print(''.join([T[S[L - 1 - i]] for i in range(L)]))
