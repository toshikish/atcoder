N = int(input())
S = list(input())

for i in range(len(S)):
    S[i] = chr(65 + (ord(S[i]) - 65 + N) % 26)
print(''.join(S))
