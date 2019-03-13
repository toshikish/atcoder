D, N = map(int, input().split())

if D == 0:
    l = [i for i in range(1, 200) if i % 100 != 0]
elif D == 1:
    l = [i for i in range(100, 20000, 100) if i % 10000 != 0]
else:
    l = [i for i in range(10000, 2000000, 10000) if i % 1000000 != 0]
print(l[N - 1])
