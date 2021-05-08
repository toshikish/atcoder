from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

R = [(A[i] % 200, i + 1) for i in range(N)]
R.sort()

ans = False
B = []
C = []
for i in range(N - 1):
    if R[i][0] == R[i + 1][0]:
        ans = True
        B.append(R[i][1])
        C.append(R[i + 1][1])
        break
else:
    dp = defaultdict(list)
    dp[0] = []
    for i in range(N):
        for k in list(dp.keys()):
            nk = (k + R[i][0]) % 200
            if nk in dp and dp[nk] != []:
                ans = True
                B = dp[k] + [R[i][1]]
                C = dp[nk]
                break
            dp[nk] = dp[k] + [R[i][1]]

if ans:
    print('Yes')
    print(' '.join(list(map(str, [len(B)] + sorted(B)))))
    print(' '.join(list(map(str, [len(C)] + sorted(C)))))
else:
    print('No')
