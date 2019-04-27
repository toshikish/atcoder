N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
print(sum([max(V[i] - C[i], 0) for i in range(N)]))
