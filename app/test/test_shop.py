from app.shop import best_shop_sum_profit_weekly, best_shop_average_profit_daily, best_shop_daily_profit, \
    worst_shop_daily_profit, top_three_daily_profit


def test_best_shop_sum_profit_weekly():
    result = best_shop_sum_profit_weekly([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]])

    assert [2, 180] == result


def test_best_shop_average_profit_daily():
    result = best_shop_average_profit_daily([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]])

    assert [2, 30] == result


def test_best_shop_daily_profit():
    result = best_shop_daily_profit([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]])

    assert [2, 30] == result


def test_worst_shop_daily_profit():
    result = worst_shop_daily_profit([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]])

    assert [0, 10] == result


def test_top_three_daily_profit():
    result = top_three_daily_profit([[10, 20, 40, 30, 5], [25, 29, 27, 30, 15, 17], [46, 50, 49, 38, 37, 30]])

    assert [[20, 30, 40], [27, 29, 30], [46, 49, 50]] == result
