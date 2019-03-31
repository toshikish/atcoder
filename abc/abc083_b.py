N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    original_i = i
    s = 0
    while i != 0:
        s += i % 10
        i //= 10
    if A <= s <= B:
        ans += original_i
print(ans)
