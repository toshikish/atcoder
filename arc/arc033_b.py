Na, Nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = len(set(A + B))
P = Na + Nb - S
print(P / S)
