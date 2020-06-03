N = int(input())
S = input()

print(sum([S.count(c) % 2 for c in 'RGB']))
