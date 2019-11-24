N, M = map(int, input().split())
S = input()

max_len = 0
for i in range(N + 1):
    if S[i] == '0':
        current_len = 0
    else:
        current_len += 1
        max_len = max(current_len, max_len)

if max_len >= M:
    ans = -1
else:
    order = []
    i = N
    while i > 0:
        c = min(M, i)
        while S[i - c] == '1':
            c -= 1
        order.append(str(c))
        i -= c
    ans = ' '.join(order[::-1])

print(ans)
