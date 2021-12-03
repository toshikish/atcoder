from collections import deque

S = input()
K = int(input())
N = len(S)

series = [0] * N
series[0] = 1 if S[0] == 'X' else 0
for i in range(1, N):
    series[i] = series[i - 1] + 1 if S[i] == 'X' else 0

if K == 0:
    ans = max(series)
else:
    ans = 0
    current = 0
    used = 0
    left = deque()
    for i in range(N):
        if S[i] == 'X':
            current += 1
        else:
            if used < K:
                current += 1
                used += 1
                left.append(i)
            else:
                l = left.popleft()
                if l > 0:
                    current -= series[l - 1]
                left.append(i)
        ans = max(current, ans)

print(ans)
