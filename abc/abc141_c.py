N, K, Q = map(int, input().split())
S = [0] * N

for i in range(Q):
    S[int(input()) - 1] += 1

for i in range(N):
    print('Yes' if K - Q + S[i] > 0 else 'No')
