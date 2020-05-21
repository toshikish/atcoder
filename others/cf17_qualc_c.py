s = input()

c = 0
l = 0
r = len(s) - 1
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x':
        l += 1
        c += 1
    elif s[r] == 'x':
        r -= 1
        c += 1
    else:
        c = -1
        break

print(c)
