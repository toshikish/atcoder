S = [input() for _ in range(4)]

S.sort()
E = ['2B', '3B', 'H', 'HR']
print('Yes' if all(S[i] == E[i] for i in range(4)) else 'No')
