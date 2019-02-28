N, A, B = map(int, input().split())

S = 0
for i in range(1, N + 1):
    original_i = i
    s = 0
    while i != 0:
        s += i % 10
        i = int(i / 10)
    if s >= A and s <= B:
        S += original_i
print(S)