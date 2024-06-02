
def combine_coins(symbol, numbers):
    return ', '.join([symbol + str(i) for i in numbers])

print(combine_coins('$', range(5)))