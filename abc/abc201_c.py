S = input()

ans = 0
for Si in range(10000):
    si = '{:04}'.format(Si)
    for i in range(10):
        if S[i] == 'o':
            if si.count(str(i)) == 0:
                break
        elif S[i] == 'x':
            if si.count(str(i)) > 0:
                break
    else:
        ans += 1

print(ans)
