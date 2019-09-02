s = input()

ans = ''
l = s[0]
n = 1
for i in range(1, len(s)):
    if s[i] == l:
        n += 1
    else:
        ans += l + str(n)
        l = s[i]
        n = 1
ans += l + str(n)
print(ans)
