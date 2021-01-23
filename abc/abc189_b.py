N, X = map(int, input().split())
V = [0] * N
P = [0] * N
for i in range(N):
    V[i], P[i] = map(int, input().split())

S = 0
X *= 100
ans = -1
for i in range(N):
    S += V[i] * P[i]
    if S > X:
        ans = i + 1
        break
print(ans)
