K = int(input())

a = 0
ans = -1
S = set()
for i in range(1, K + 1):
    a = a * 10 + 7
    a %= K
    if a == 0:
        ans = i
        break
    elif a in S:
        break
    S.add(a)
print(ans)
