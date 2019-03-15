N = int(input())
S = input()

original_w = []
prev = 0
for i in range(N):
    if S[i] == 'W':
        prev += 1
    original_w.append(prev)

original_e = []
prev = 0
for i in range(N - 1, -1, -1):
    if S[i] == 'E':
        prev += 1
    original_e.append(prev)

ans = min(original_e[N - 1], original_w[N - 2])
for i in range(1, N - 1):
    ans = min(ans, original_w[i - 1] + original_e[N - (i + 1)])
print(ans)

