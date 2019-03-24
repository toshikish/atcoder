N = int(input())
s = 'MARCH'
c = [0] * 5
for i in range(N):
    S = input()
    for j in range(5):
        if S[0] == s[j]:
            c[j] += 1

ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += c[i] * c[j] * c[k]
print(ans)
