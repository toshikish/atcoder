N = int(input())
A = list(map(int, input().split()))

B = [(A[i], i + 1) for i in range(N)]
B.sort()
print(B[-2][1])
