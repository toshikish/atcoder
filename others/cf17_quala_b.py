N, M, K = map(int, input().split())

ans = False
for n in range(N + 1):
    for m in range(M + 1):
        if n * (M - m) + m * (N - n) == K:
            ans = True
            break
    else:
        continue
    break
print('Yes' if ans else 'No')
