a0 = 100
a1 = 100
a2 = 200
for i in range(17):
    t = a0 + a1 + a2
    a0 = a1
    a1 = a2
    a2 = t
print(a2)
