N = int(input())

S = 0
for i in range(N):
    Ai, Bi = map(int, input().split())
    S += (Ai + Bi) * (Bi - Ai + 1) // 2
print(S)
