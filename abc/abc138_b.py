N = int(input())
A = list(map(int, input().split()))
print(1 / sum([1 / Ai for Ai in A]))
