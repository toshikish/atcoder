import bisect

N = int(input())
A = list(map(int, input().split()))

acc_A = [0]
for i in range(N):
    acc_A.append(acc_A[-1] + A[i])
acc_A.append(acc_A[-1])
half = acc_A[-1] / 2
mid = bisect.bisect_left(acc_A, half)

if acc_A[mid] == half:
    ans = 0
else:
    ans = min(abs((acc_A[mid] - acc_A[0]) - (acc_A[-1] - acc_A[mid])),
              abs((acc_A[mid - 1] - acc_A[0]) - (acc_A[-1] - acc_A[mid - 1])))
print(ans)
