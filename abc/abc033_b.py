N = int(input())
max_S = ''
max_P = 0
sum_P = 0
for i in range(N):
    Si, Pi = input().split()
    Pi = int(Pi)
    sum_P += Pi
    if Pi > max_P:
        max_S = Si
        max_P = Pi

print(max_S if max_P > sum_P // 2 else 'atcoder')
