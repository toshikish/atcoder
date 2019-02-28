L = int(input())
A = []
for i in range(L):
    A.append(int(input()))

while A[0] == 0:
    A.pop(0)
while A[-1] == 0:
    A.pop(-1)

x = 0
for a in A:
    if a % 2 == 0:
        x += 1
print(x)