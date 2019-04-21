N = int(input())
S = input()

w = [0]
w_total = 0
b = [0]
b_total = 0
for i in range(N):
    if S[i] == '#':
        w_total += 1
    w.append(w_total)
    if S[N - 1 - i] == '.':
        b_total += 1
    b.append(b_total)

ans = N + 1
for i in range(N + 1):
    ans = min(ans, w[i] + b[N - i])
print(ans)
