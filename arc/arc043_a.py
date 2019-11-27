N, A, B = map(int, input().split())
S = [int(input()) for i in range(N)]

sum_S = sum(S)
max_S = max(S)
min_S = min(S)

if max_S == min_S:
    print(-1)
else:
    P = B / (max_S - min_S)
    Q = A - P * sum_S / N
    print(P, Q)
