N, K = map(int, input().split())
S = input()

seq = [1] if S[0] == '1' else [0, 1]
for i in range(1, N):
    if S[i - 1] == S[i]:
        seq[-1] += 1
    else:
        seq.append(1)
if S[N - 1] == '0':
    seq.append(0)

n0 = (len(seq) - 1) // 2
if n0 <= K:
    ans = N
else:
    total = [0]
    for s in seq:
        total.append(total[-1] + s)

    ans = 0
    for i in range(n0 - K + 1):
        ans = max(ans, total[(i + K) * 2 + 1] - total[i * 2])

print(ans)
