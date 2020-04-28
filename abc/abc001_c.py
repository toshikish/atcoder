import bisect

Deg, Dis = map(int, input().split())

L_dir = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
         'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
Dir = L_dir[((Deg * 10 + 1125) // 2250) % 16]

V_w = list(
    map(lambda x: x * 60, [25, 155, 335, 545, 795, 1075, 1385, 1715, 2075, 2445, 2845, 3265]))
W = bisect.bisect_right(V_w, Dis * 100)

if W == 0:
    Dir = 'C'
print(Dir, W)
