c = []
for i in range(4):
    c.append(input().split())

for i in range(4):
    print(' '.join(c[3 - i][::-1]))
