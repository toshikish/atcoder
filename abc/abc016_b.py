A, B, C = map(int, input().split())

if B == 0:
    if A == C:
        ans = '?'
    else:
        ans = '!'
else:
    if A + B == C:
        ans = '+'
    elif A - B == C:
        ans = '-'
    else:
        ans = '!'
print(ans)
