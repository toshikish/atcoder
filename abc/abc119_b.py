rate = 380000.0
sum_jpy = 0.0

N = int(input())
for i in range(N):
    x, u = input().rstrip().split()
    x = float(x)
    if u == 'BTC':
        x = x * rate
    sum_jpy += x

print(sum_jpy)