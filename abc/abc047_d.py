N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
temp_min = A[0]
max_diff = 0
for i in range(1, N):
    if A[i] < temp_min:
        temp_min = A[i]
    else:
        diff = A[i] - temp_min
        if diff > max_diff:
            ans = 1
            max_diff = diff
        elif diff == max_diff:
            ans += 1
print(ans)
