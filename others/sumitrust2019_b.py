N = int(input())

print(int((N + 1) / 1.08)
      if 100 * N % 108 == 0 or 100 * (N + 1) % 108 != 0 and int(N / 1.08) + 1 == int((N + 1) / 1.08) else ':(')
