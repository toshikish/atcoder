H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

m = min([min(Ai) for Ai in A])
print(sum([sum([Aij - m for Aij in Ai]) for Ai in A]))
