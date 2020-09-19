N = int(input())
c = 0
ans = False
for i in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        c += 1
    else:
        c = 0
    if c >= 3:
        ans = True
print('Yes' if ans else 'No')