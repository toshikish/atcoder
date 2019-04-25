H, W = map(int, input().split())
a = [input() for i in range(H)]

print('#' * (W + 2))
for ai in a:
    print('#{}#'.format(ai))
print('#' * (W + 2))
