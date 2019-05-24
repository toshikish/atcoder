W, H, N = map(int, input().split())

x_min = y_min = 0
x_max = W
y_max = H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    else:
        y_max = min(y_max, y)
print(max(x_max - x_min, 0) * max(y_max - y_min, 0))
