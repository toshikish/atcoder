import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
for b in B:
    i_a = bisect.bisect_left(A, b)
    i_c = bisect.bisect_right(C, b)
    ans += i_a * (N - i_c)
print(ans)
