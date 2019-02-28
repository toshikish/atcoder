N = int(input())
A = input()
B = input()
C = input()
x = 0
for i in range(N):
    letters = len({A[i], B[i], C[i]})
    if letters == 2:
        x += 1
    elif letters == 3:
        x += 2
print(x)
