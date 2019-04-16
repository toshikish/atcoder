N = int(input())
p = list(map(int, input().split())) + [0]

counter = 0
seq = 0
for i in range(N + 1):
    if p[i] == i + 1:
        seq += 1
    elif seq != 0:
        counter += (seq + 1) // 2    
        seq = 0
print(counter)
