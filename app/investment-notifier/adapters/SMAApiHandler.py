import asyncio
import os

import aiohttp

from domain.Investment import Investment
from services.sma_calculator import StockSMA


class SMAApiHandler:
    # TODO - could swap for SSM
    base_url = os.getenv("SMA_BASE_URL")
    api_key = os.getenv("SMA_API_KEY")

    async def get_sma_for_stock(
            self,
            client_session: aiohttp.ClientSession,
            investment: Investment,
            interval: str = "daily",
            period: int = 200,
            limit: int = 365
    ) -> StockSMA:
        query_params = {
            "function": "SMA",
            "symbol": f"{investment.ticker}.LON",
            "interval": interval,
            "time_period": period,
            "series_type": "close",
            "apikey": self.api_key
        }

        sma_values = []

        async with client_session.get(
            f"{self.base_url}query",
            params=query_params
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

    async def _get_sma_tasks_for_stocks(self, investments: [Investment]) -> [StockSMA]:
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(*[
                self.get_sma_for_stock(session, investment) for investment in investments
            ])

    def get_smas_for_investments(self, investments: [Investment]) -> [StockSMA]:
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(self._get_sma_tasks_for_stocks(investments))
        loop.close()

        return results
