A, B = map(int, input().split())

if A >= 990 and B <= 109:
    ans = max(999 - B, A - 100)
elif A >= 900 and B <= 199:
    ans = max((990 + A % 10) - B, A - (100 + B % 10))
else:
    ans = max((900 + A % 100) - B, A - (100 + B % 100))
print(ans)
