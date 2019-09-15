S = input()

weathers = ['Sunny', 'Cloudy', 'Rainy']
print(weathers[(weathers.index(S) + 1) % 3])
