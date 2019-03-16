def best_shop_sum_profit_weekly(shops):
    total_profit = []

    for shop in shops:
        shop_profit = 0

        for s in shop:
            shop_profit += s
        total_profit.append(shop_profit)

    max_profit = max(total_profit)
    index = total_profit.index(max_profit)
    return [index, int(max_profit)]


def best_shop_average_profit_daily(shops):
    total_profit = []

    for shop in shops:
        shop_profit = 0

        for s in shop:
            shop_profit += s
        average_daily_profit = shop_profit / len(shop)
        total_profit.append(average_daily_profit)
    max_average_profit = max(total_profit)
    index = total_profit.index(max_average_profit)
    return [index, int(max_average_profit)]


def best_shop_daily_profit(shops):
    best_daily_profit = []

    for shop in shops:
        best_daily_profit.append(max(shop))
    best_profit = max(best_daily_profit)
    index = best_daily_profit.index(best_profit)
    return [index, int(best_profit)]


def worst_shop_daily_profit(shops):
    worst_daily_profit = []

    for shop in shops:
        worst_daily_profit.append(max(shop))
    worst_profit = min(worst_daily_profit)
    index = worst_daily_profit.index(worst_profit)
    return [index, int(worst_profit)]


def top_three_daily_profit(shops):
    top_three_profit = []

    for shop in shops:
        shop.sort()
        top = shop[-3:]
        top_three_profit.append(top)
    return top_three_profit

