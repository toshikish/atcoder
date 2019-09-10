A, B, C = map(int, input().split())

if A == B == C:
    ans = -1 if A % 2 == 0 else 0
else:
    ans = 0
    while A % 2 + B % 2 + C % 2 == 0:
        A, B, C = (B + C) // 2, (C + A) // 2, (A + B) // 2
        ans += 1
print(ans)
