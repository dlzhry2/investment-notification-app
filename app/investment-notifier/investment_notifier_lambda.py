import os

from HLInvestmentNotifier import HLInvestmentNotifier
from adapters.SMAApiHandler import SMAApiHandler
from adapters.aws.SNSAdapter import SNSAdapter
from web_drivers.HLDriver import HLDriver

RECOMMENDED_INVESTMENTS = "recommended investments"
NET_GAIN_LOSS = "net gain/loss"
PERMITTED_REPORTS = [RECOMMENDED_INVESTMENTS, NET_GAIN_LOSS]
INVESTMENT_REC_NO = int(os.getenv("INVESTMENT_REC_NO"))
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

api_handler = SMAApiHandler()
web_driver = HLDriver()
notification_adapter = SNSAdapter()

notifier_app = HLInvestmentNotifier(
    api_handler,
    web_driver,
    notification_adapter,
    SNS_TOPIC_ARN
)


def handler(event, context):
    requested_report = event.get("report")

    if requested_report not in PERMITTED_REPORTS:
        raise NotImplementedError("Requested report does not exist")

    if requested_report == NET_GAIN_LOSS:
        notifier_app.report_overall_gain_loss()

    elif requested_report == RECOMMENDED_INVESTMENTS:
        notifier_app.report_best_next_investments(INVESTMENT_REC_NO)

    return True
