s = input()

k = 'keyence'
ans = False
for i in range(8):
    if k[0:i] == s[0:i] and k[i:8] == s[-(7 - i):]:
        ans = True
        break
print('YES' if ans else 'NO')
