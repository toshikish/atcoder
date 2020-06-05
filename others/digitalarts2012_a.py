s = input().split()
N = int(input())
t = [input() for i in range(N)]

ans = []
for si in s:
    for ti in t:
        if len(si) != len(ti):
            continue
        if all(si[i] == ti[i] or ti[i] == '*' for i in range(len(si))):
            ans.append('*' * len(si))
            break
    else:
        ans.append(si)
print(' '.join(ans))
