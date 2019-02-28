y, m, d = list(map(int, input().rstrip().split('/')))

if y <= 2018 or (y == 2019 and m <= 4):
    print('Heisei')
else:
    print('TBD')