S = list(input())
a, b = map(lambda s: int(s) - 1, input().split())

S[a], S[b] = S[b], S[a]
print(''.join(S))
