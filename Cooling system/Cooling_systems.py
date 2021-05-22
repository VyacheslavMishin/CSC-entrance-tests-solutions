def minimal_price(costs_and_powers, minimal_powers):
    price_list, total_price, current_model = sorted(list(costs_and_powers.keys())), 0, 0
    minimal_powers.sort()

    for min_power in minimal_powers:
        while costs_and_powers[price_list[current_model]] < min_power:
            current_model += 1
        total_price += price_list[current_model]

    return total_price


aud_number = int(input())
min_powers = list(map(int, input().split()))
models = int(input())
prices_and_powers = dict()

for model in range(models):
    power, price = list(map(int, input().split()))
    prices_and_powers[price] = max(prices_and_powers.get(price, 0), power)

print(minimal_price(prices_and_powers, min_powers))
