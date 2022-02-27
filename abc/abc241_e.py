N, K = map(int, input().split())
A = list(map(int, input().split()))

visited = [-1] * N
total = [0]
X = 0
i = 0
c = 0
while visited[i] == -1:
    visited[i] = c
    X += A[i]
    total.append(X)
    i = X % N
    c += 1

init = visited[i]
loop = c - visited[i]
if K <= init:
    ans = total[K]
else:
    over = K - init
    ans = (over // loop) * (total[-1] - total[init]) \
        + total[init + over % loop]
print(ans)
