from math import gcd

N = int(input())
A = list(map(int, input().split()))

cum_left = [A[0]]
cum_right = [A[N - 1]]
for i in range(1, N - 1):
    cum_left.append(gcd(cum_left[-1], A[i]))
    cum_right.append(gcd(cum_right[-1], A[N - 1 - i]))

ans = max(cum_left[N - 2], cum_right[N - 2])
for i in range(1, N - 1):
    ans = max(ans, gcd(cum_left[i - 1], cum_right[N - 2 - i]))
print(ans)
