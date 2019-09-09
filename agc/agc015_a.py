N, A, B = map(int, input().split())
if N == 1 and A != B or A > B:
    ans = 0
else:
    ans = (N - 2) * (B - A) + 1
print(ans)
