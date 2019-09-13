N = int(input())
odd = len(list(filter(lambda x: int(x) % 2, input().split())))
even = N - odd

even += odd // 2
even %= 2
odd %= 2

print('NO' if odd == even == 1 else 'YES')
