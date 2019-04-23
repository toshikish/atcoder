N = int(input())
s = []
subtractable = []
total = 0
for i in range(N):
    si = int(input())
    s.append(si)
    if si % 10 != 0:
        subtractable.append(si)
    total += si
if total % 10 != 0:
    ans = total
else:
    if subtractable == []:
        ans = 0
    else:
        subtractable.sort()
        ans = total - subtractable[0]
print(ans)
