N = int(input())
a = [int(input()) for i in range(N)]
print('second' if all(ai % 2 == 0 for ai in a) else 'first')
