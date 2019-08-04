N = int(input())
H = list(map(int, input().split()))

ans = True
h = H[0]
decreaseable = True
for i in range(1, N):
    if H[i] <= H[i - 1] - 2 or not decreaseable and H[i] < h:
        ans = False
        break
    if H[i] == h - 1:
        h = H[i]
        decreaseable = False
    elif H[i] > h:
        h = H[i]
        decreaseable = True
print('Yes' if ans else 'No')
