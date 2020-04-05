N, M, K = map(int, input().split())

ans = False
for n in range(N + 1):
    if 2 * n == N:
        if M * n == K:
            ans = True
            break
    else:
        num = M * n - K
        denom = 2 * n - N
        if num % denom == 0 and 0 <= num // denom <= M:
            ans = True
            break
print('Yes' if ans else 'No')
