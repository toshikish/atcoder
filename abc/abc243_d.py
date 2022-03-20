N, X = map(int, input().split())
S = input()

L = list(bin(X))
for Si in S:
    if Si == 'U':
        L.pop()
    elif Si == 'L':
        L.append('0')
    else:
        L.append('1')

print(int(''.join(L), 2))
