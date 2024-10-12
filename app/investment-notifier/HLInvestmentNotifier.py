from adapters.SMAApiHandler import SMAApiHandler
from domain.Investment import Investment
from services.InvestmentNotifier import InvestmentNotifier
from web_drivers.HLDriver import HLDriver


class HLInvestmentNotifier(InvestmentNotifier):

    def report_best_next_investments(self, top_x: int = 3) -> [Investment]:
        investments = self.investments_web_driver.get_investments()
        sma_data = self.sma_service.get_smas_for_investments(investments)

        sma_data.sort(key=lambda x: x.rate_of_change, reverse=True)
        top_x = sma_data[: top_x]
        print("Gathering top investment options:")

        for item in top_x:
            print(f"{item.investment.name} ({item.investment.ticker}) - 200 Day SMA rate of change = {item.rate_of_change}")

        # next step - test and fix up any problematic functionality
        # NS adapter and actually publish the message
        pass

    def report_overall_gain_loss(self) -> str:
        gain_loss = self.investments_web_driver.get_all_time_percentage_change()

        # TODO - make a nice notification message
        print("Some notification: " + gain_loss)
        return gain_loss


api_handler = SMAApiHandler()
web_driver = HLDriver()
test_driver = HLInvestmentNotifier(api_handler, web_driver)

# test_driver.report_best_next_investments(5)
test_driver.report_overall_gain_loss()
