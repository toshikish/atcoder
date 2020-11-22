r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


s1 = r1 + c1
d1 = r1 - c1
s2 = r2 + c2
d2 = r2 - c2
if (r1, c1) == (r2, c2):
    ans = 0
elif s1 == s2 or d1 == d2 or manhattan((r1, c1), (r2, c2)) <= 3:
    ans = 1
elif (r1 + c1) % 2 == (r2 + c2) % 2:
    ans = 2
else:
    ans = 3
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) > 3:
                continue
            r3, c3 = r1 + i, c1 + j
            s3 = r3 + c3
            d3 = r3 - c3
            if s2 == s3 or d2 == d3:
                ans = 2
                break
        else:
            continue
        break
print(ans)
