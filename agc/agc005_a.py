X = input()

s = 0
ans = 0
for Xi in X:
    if Xi == 'S':
        s += 1
        ans += 1
    else:
        if s >= 1:
            s -= 1
            ans -= 1
        else:
            ans += 1
print(ans)
