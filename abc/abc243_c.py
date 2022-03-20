from collections import defaultdict

N = int(input())
d = defaultdict(list)
for i in range(N):
    Xi, Yi = map(int, input().split())
    d[Yi].append((Xi, i))
S = input()

ans = False
for _, xs in d.items():
    rightward = False
    xs.sort()
    for _, i in xs:
        if S[i] == 'R':
            rightward = True
        elif rightward:
            ans = True
            break
    else:
        continue
    break

print('Yes' if ans else 'No')
