N = int(input())
x = [input() for i in range(N)]

ans = 0
for i in range(9):
    prev = '.'
    for j in range(N):
        if x[j][i] == 'x':
            ans += 1
            prev = 'x'
        elif x[j][i] == 'o':
            if prev != 'o':
                ans += 1
            prev = 'o'
        else:
            prev = '.'
print(ans)
