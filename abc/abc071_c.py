from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

bars = defaultdict(int)
for a in A:
    bars[a] += 1

sides = list(bars.keys())
sides.sort(reverse=True)
ans = 0
rect = []
for side in sides:
    if bars[side] >= 4:
        if rect == []:
            ans = side * side
        else:
            ans = rect[0] * side
        break
    elif bars[side] >= 2:
        rect.append(side)
        if len(rect) == 2:
            ans = rect[0] * rect[1]
            break
print(ans)
