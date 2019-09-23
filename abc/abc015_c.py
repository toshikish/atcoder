N, K = map(int, input().split())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))

possible = False
for i in range(K ** N):
    v = 0
    for j in range(N):
        v ^= T[j][i % K]
        i //= K
    if v == 0:
        possible = True
        break
print('Found' if possible else 'Nothing')
