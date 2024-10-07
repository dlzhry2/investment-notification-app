from domain.Investment import Investment
from services.InvestmentNotifier import InvestmentNotifier


class HLInvestmentNotifier(InvestmentNotifier):

    def report_best_next_investments(self) -> [Investment]:
        investments = self.investments_web_driver.get_investments()
        # TODO
        # implement SMA API Handler - retrieves for a given ticker + tests
        # investment calculator utils: implement logic for rate of change
        # helper function - in here? - to orchestrate both of the above for a ticker
        # in this function, gather tasks and make async
        # log the notification message and return top x
        # need the top x as an argument
        # next step - SNS adapter and actually publish the message
        pass

    def report_overall_gain_loss(self) -> str:
        gain_loss = self.report_overall_gain_loss()

        # TODO - make a nice notification message
        print("Some notification: " + gain_loss)
        return gain_loss
