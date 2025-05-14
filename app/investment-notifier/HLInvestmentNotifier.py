from services.InvestmentNotifier import InvestmentNotifier
from services.sma_calculator import StockSMA


class HLInvestmentNotifier(InvestmentNotifier):

    def report_best_next_investments(self, top_x: int = 3) -> list[StockSMA]:
        investments = self.investments_web_driver.get_investments()
        sma_data = self.sma_service.get_smas_for_investments(investments)

        sma_data.sort(key=lambda x: x.rate_of_change, reverse=True)
        top_x_investment_options = sma_data[: top_x]
        message = ""
        print("Gathering top investment options: ")

        for item in top_x_investment_options:
            investment_recommendation = (f"{item.investment.name} ({item.investment.ticker}) - 200 Day SMA rate of "
                                         f"change = {item.rate_of_change}\n")
            message = message + investment_recommendation

        self.notification_adapter.notify(
            self.notification_endpoint,
            message
        )

        return top_x_investment_options

    def report_overall_gain_loss(self) -> str:
        gain_loss = self.investments_web_driver.get_all_time_percentage_change()

        message = f"Total Account Gain/Loss: {gain_loss}"
        print(f"Sending message to sns: {message}")

        self.notification_adapter.notify(
            self.notification_endpoint,
            message
        )

        return gain_loss
