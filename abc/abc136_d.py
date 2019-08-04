S = input()

N = len(S)
A = [0] * N
start_r = 0
for i in range(1, N):
    if S[i - 1:i + 1] == 'RL':
        r = i - 1
        l = i
        A[i - 1] += 1
        A[i] += 1
        if start_r < r:
            d = r - start_r
            A[i - 1] += d // 2
            A[i] += d // 2 + d % 2
    elif S[i - 1:i + 1] == 'LR':
        start_r = i
    elif S[i - 1:i + 1] == 'LL':
        A[r + (i - l + 1) % 2] += 1
print(' '.join(list(map(str, A))))
