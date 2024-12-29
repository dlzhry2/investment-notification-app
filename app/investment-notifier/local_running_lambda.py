import os

from HLInvestmentNotifier import HLInvestmentNotifier
from adapters.SMAApiHandler import SMAApiHandler
from adapters.local.LocalNotificationAdapter import LocalNotificationAdapter
from web_drivers.HLDriver import HLDriver

INVESTMENT_REC_NO = int(os.getenv("INVESTMENT_REC_NO"))
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

api_handler = SMAApiHandler()
web_driver = HLDriver()
notification_adapter = LocalNotificationAdapter()

notifier_app = HLInvestmentNotifier(
    api_handler,
    web_driver,
    notification_adapter,
    SNS_TOPIC_ARN
)


if __name__ == "__main__":
    notifier_app.report_overall_gain_loss()
    notifier_app.report_best_next_investments(INVESTMENT_REC_NO)
