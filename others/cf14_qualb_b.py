N = input()[::-1]
print(sum(list(map(int, N[1::2]))), sum(list(map(int, N[0::2]))))
