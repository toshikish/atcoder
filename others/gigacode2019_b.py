N, X, Y, Z = map(int, input().split())
S = [tuple(map(int, input().split())) for i in range(N)]

print(sum([Ai >= X and Bi >= Y and Ai + Bi >= Z for Ai, Bi in S]))
