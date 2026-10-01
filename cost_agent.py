def cost_analysis(prices):

    cheapest_period = min(
        prices,
        key=prices.get
    )

    cheapest_price = prices[cheapest_period]

    return {
        "prices": prices,
        "cheapest_period": cheapest_period,
        "cheapest_price": cheapest_price
    }