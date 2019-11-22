S = input()

d = {'Left': '<', 'Right': '>', 'AtCoder': 'A'}
T = []
for s in S.split():
    T.append(d[s])
print(' '.join(T))
