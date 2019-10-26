a, b = map(int, input().split())

if a <= 0 <= b:
    ans = 'Zero'
elif 0 < a or b < 0 and (b - a) % 2 == 1:
    ans = 'Positive'
else:
    ans = 'Negative'
print(ans)
