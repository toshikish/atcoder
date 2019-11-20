N, L = map(int, input().split())
S = input()

t = 1
ans = 0
for s in S:
    if s == '+':
        t += 1
        if t > L:
            ans += 1
            t = 1
    else:
        t -= 1
print(ans)
