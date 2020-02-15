C = int(input())
N, M, L = [], [], []

for i in range(C):
    Ni, Mi, Li = sorted(list(map(int, input().split())))
    N.append(Ni)
    M.append(Mi)
    L.append(Li)

print(max(N) * max(M) * max(L))
