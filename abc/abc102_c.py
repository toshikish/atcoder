import statistics
N = int(input())
A = list(map(int, input().split()))

B = [A[i] - (i + 1) for i in range(N)]
B.sort()
b = int(statistics.median(B))
print(sum([abs(B[i] - b) for i in range(N)]))
