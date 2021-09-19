X = int(input())

if X >= 90:
    ans = 'expert'
elif X < 40:
    ans = 40 - X
elif X < 70:
    ans = 70 - X
else:
    ans = 90 - X
print(ans)
