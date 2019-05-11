N = int(input())
ans = n_BA = n_A = n_B = n_others = 0
for i in range(N):
    s = input()
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        n_BA += 1
    elif s[0] == 'B':
        n_B += 1
    elif s[-1] == 'A':
        n_A += 1
    else:
        n_others += 1

if n_BA >= 1:
    ans += n_BA - 1
    if n_A >= 1:
        n_A -= 1
        ans += 1
    if n_B >= 1:
        n_B -= 1
        ans += 1
ans += min(n_A, n_B)
print(ans)
