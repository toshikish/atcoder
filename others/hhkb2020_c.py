N = int(input())
p = list(map(int, input().split()))

pointer = 0
v = [False] * 200001
for pi in p:
    v[pi] = True
    while v[pointer]:
        pointer += 1
    print(pointer)
