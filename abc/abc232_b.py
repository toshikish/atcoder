S = input()
T = input()

K = (ord(T[0]) - ord(S[0])) % 26
ans = all((ord(T[i]) - ord(S[i])) % 26 == K for i in range(len(S)))
print('Yes' if ans else 'No')
