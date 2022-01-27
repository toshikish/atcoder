from itertools import accumulate

X = list(map(int, list(input())))
Y = list(accumulate(X))
N = len(X)

ans = []
res = 0
for i in range(N - 1, -1, -1):
    di = Y[i] + res
    ans.append(str(di % 10))
    res = di // 10
if res > 0:
    ans.append(str(res))
print(''.join(ans[::-1]))
