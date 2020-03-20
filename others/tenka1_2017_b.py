N = int(input())
P = {}
for i in range(N):
    Ai, Bi = map(int, input().split())
    P[Ai] = Bi
k = max(P.keys())
print(k + P[k])
