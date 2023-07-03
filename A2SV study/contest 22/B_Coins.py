
coin_weights = {key: 0 for key in 'ABC'}

for i in range(3):

    coin1, relation, coin2 = map(str, input().strip())
    if relation == '>':
        coin_weights[coin1] += 1
    else:
        coin_weights[coin2] += 1

sorted_coins = sorted(coin_weights, key=coin_weights.get)
if coin_weights[sorted_coins[0]] == coin_weights[sorted_coins[1]] or coin_weights[sorted_coins[1]] == coin_weights[sorted_coins[2]]:
    result = 'Impossible'
else:
    result = ''.join(sorted_coins)

print(result)