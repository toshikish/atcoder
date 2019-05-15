N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = []
X = []
for i in range(M):
    Pi, Xi = map(int, input().split())
    P.append(Pi)
    X.append(Xi)

S = sum(T)
for i in range(M):
    print(S - (T[P[i] - 1] - X[i]))
