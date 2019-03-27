N = int(input())
t = [0]
x = [0]
y = [0]
for i in range(N):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)

def judge():
    for i in range(N):
        dt = t[i + 1] - t[i]
        diff = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
        if diff > dt or (dt - diff) % 2 != 0:
            return False
    return True

print('Yes' if judge() else 'No')
