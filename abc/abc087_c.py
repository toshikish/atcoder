N = int(input())
U = list(map(int, input().split()))
L = list(map(int, input().split()))

sumU = [U[0]]
for i in range(1, N):
    sumU.append(sumU[-1] + U[i])
sumL = [L[N - 1]]
for i in range(N - 2, -1, -1):
    sumL.insert(0, sumL[0] + L[i])

print(max([sumU[i] + sumL[i] for i in range(N)]))
