N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

c = [0] * 3
for Pi in P:
    if Pi <= A:
        c[0] += 1
    elif Pi <= B:
        c[1] += 1
    else:
        c[2] += 1
print(min(c))
