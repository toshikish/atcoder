N = int(input())
R = [tuple(map(int, input().split())) for i in range(N)]
B = [tuple(map(int, input().split())) for i in range(N)]

R.sort(key=lambda r: r[1], reverse=True)
B.sort()

ans = 0
for b in B:
    for r in R:
        if r[0] < b[0] and r[1] < b[1]:
            ans += 1
            R.remove(r)
            break
print(ans)
