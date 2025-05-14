import asyncio
import os

import aiohttp

from collections.abc import Iterable

from domain.Investment import Investment
from services.sma_calculator import StockSMA


class SMAApiHandler:
    def __init__(self, api_key):
        self.base_url = os.getenv("SMA_BASE_URL")
        self.api_key = api_key

    async def get_sma_for_stock(
        self,
        client_session: aiohttp.ClientSession,
        investment: Investment,
        interval: str = "daily",
        period: int = 200,
        limit: int = 365,
    ) -> StockSMA:
        query_params = {
            "function": "SMA",
            "symbol": f"{investment.ticker}.LON",
            "interval": interval,
            "time_period": period,
            "series_type": "close",
            "apikey": self.api_key,
        }

        sma_values = []

        async with client_session.get(
            f"{self.base_url}query", params=query_params
        ) as response:
            parsed_response = await response.json()
            sma_data = parsed_response.get("Technical Analysis: SMA", {})
            iterator = 0

            for item in sma_data.items():
                if iterator > limit:
                    break

                iterator = iterator + 1
                _date, data = item
                sma_values.append(float(data.get("SMA")))

            return StockSMA(investment, sma_values)

    async def _get_sma_tasks_for_stocks(
        self, investments: Iterable[Investment]
    ) -> list[StockSMA]:
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(
                *[
                    self.get_sma_for_stock(session, investment)
                    for investment in investments
                ]
            )

    def get_smas_for_investments(
        self, investments: Iterable[Investment]
    ) -> list[StockSMA]:
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(self._get_sma_tasks_for_stocks(investments))
        loop.close()

        return results
