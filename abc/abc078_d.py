N, Z, W = map(int, input().split())
if N == 1:
    a = int(input())
    print(abs(a - W))
else:
    a = list(map(int, input().split()))
    print(max(abs(a[N - 1] - W), abs(a[N - 2] - a[N - 1])))
