N = int(input())

n = N % 10
print('hon' if n in [2, 4, 5, 7, 9] else 'pon' if n in [0, 1, 6, 8] else 'bon')
