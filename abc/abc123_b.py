A = [int(input()) for i in range(5)]

dec = 0
m = 10
for a in A:
    dec += a // 10
    if a % 10 > 0:
        dec += 1
        m = min(m, a % 10)
print(10 * (dec - 1) + m)
