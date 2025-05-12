from domain.Investment import Investment

DOWNWARD_TREND = "down"
UPWARD_TREND = "up"


class StockSMA:
    def __init__(self, investment: Investment, sma_list: list[float]):
        # TODO - feat. in future could make this smarter and handle different periods
        self.investment = investment
        # Ordered chronologically descending
        self.sma_list = sma_list
        self.rate_of_change = calculate_rate_of_change(self.sma_list)


def calculate_rate_of_change(sma_list: list[float]) -> float:
    # TODO - handle list being empty and sort out mypy
    trend = find_starting_trend(sma_list)
    days = 1
    end_price = sma_list[0]
    start_price = None

    if trend == UPWARD_TREND:
        for i in range(len(sma_list) - 1):
            if sma_list[i + 1] > sma_list[i]:
                break
            days = days + 1
            start_price = sma_list[i + 1]

    elif trend == DOWNWARD_TREND:
        for i in range(len(sma_list) - 1):
            if sma_list[i + 1] < sma_list[i]:
                break
            days = days + 1
            start_price = sma_list[i + 1]

    rate_of_percentage_range = (((end_price - start_price) / end_price) * 100) / days
    return round(rate_of_percentage_range, 4)


def find_starting_trend(sma_list: list[float]) -> str:
    for i in range(len(sma_list) - 1):
        diff = sma_list[i] - sma_list[i + 1]

        if diff == 0:
            continue

        return UPWARD_TREND if diff > 0 else DOWNWARD_TREND

    raise Exception("All SMA values were the same. Please check API")
