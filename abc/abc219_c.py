X = input()
N = int(input())
S = [input() for _ in range(N)]

D = {}
for i in range(26):
    D[X[i]] = chr(ord('a') + i)

T = []
for Si in S:
    Ti = ''.join([D[l] for l in Si])
    T.append((Ti, Si))
T.sort()
for Ti in T:
    print(Ti[1])
