N = int(input())

max_n = 0
max_times = -1
for i in range(1, N + 1):
    times = 0
    original_i = i
    while i % 2 == 0:
        i //= 2
        times += 1
    if times >= max_times:
        max_n = original_i
        max_times = times
print(max_n)
