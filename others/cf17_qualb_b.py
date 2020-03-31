from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

cd = Counter(D)
ct = Counter(T)

ans = True
for i in ct.keys():
    if cd[i] < ct[i]:
        ans = False
        break
print('YES' if ans else 'NO')
