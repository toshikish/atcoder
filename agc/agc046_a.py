X = int(input())

K = 1
while True:
    if K * X % 360 == 0:
        break
    K += 1
print(K)
