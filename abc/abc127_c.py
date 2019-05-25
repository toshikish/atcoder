N, M = map(int, input().split())
L = []
R = []
for i in range(M):
    Li, Ri = map(int, input().split())
    L.append(Li)
    R.append(Ri)

print(max(0, min(R) - max(L) + 1))
