def coinCombination(total):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (total + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, total + 1):
            ways[amount] += ways[amount - coin]

    return ways[total]

print(coinCombination(200))  