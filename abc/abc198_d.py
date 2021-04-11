from itertools import permutations

S = [input() for _ in range(3)]

T = [[] for _ in range(3)]
d = dict()
l = 0
for i in range(3):
    Si = S[i]
    Ti = T[i]
    for Sij in Si:
        if Sij not in d:
            d[Sij] = l
            l += 1
        Ti.append(d[Sij])
solvable = l <= 10

if solvable:
    msb = [T[i][0] for i in range(3)]
    for p in permutations('0123456789', l):
        if any([p[i] == '0' for i in msb]):
            continue
        N1 = int(''.join([p[Ti] for Ti in T[0]]))
        N2 = int(''.join([p[Ti] for Ti in T[1]]))
        N3 = int(''.join([p[Ti] for Ti in T[2]]))
        if N1 + N2 == N3:
            solvable = True
            N = (N1, N2, N3)
            break
    else:
        solvable = False

if solvable:
    for Ni in N:
        print(Ni)
else:
    print('UNSOLVABLE')
