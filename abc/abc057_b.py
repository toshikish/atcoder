N, M = map(int, input().split())
students = [tuple(map(int, input().split())) for i in range(N)]
points = [tuple(map(int, input().split())) for i in range(M)]

for s in students:
    min_d = 10 ** 10
    min_p = 100
    for i in range(M):
        d = abs(points[i][0] - s[0]) + abs(points[i][1] - s[1])
        if d < min_d:
            min_d = d
            min_p = i
    print(min_p + 1)
