V, A, B, C = map(int, input().split())

V %= A + B + C
if V < A:
    ans = 'F'
elif V < A + B:
    ans = 'M'
else:
    ans = 'T'
print(ans)
