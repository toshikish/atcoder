s = input()

ans = ''
for k in s:
    if k == '0':
        ans += '0'
    elif k == '1':
        ans += '1'
    elif ans != '':
        ans = ans[:len(ans) - 1]
print(ans)
