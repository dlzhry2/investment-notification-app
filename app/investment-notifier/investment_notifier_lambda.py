import os

from HLInvestmentNotifier import HLInvestmentNotifier
from adapters.SMAApiHandler import SMAApiHandler
from adapters.aws.SNSAdapter import SNSAdapter
from adapters.aws.SSMAdapter import SSMAdapter
from consts.param_consts import SSM_API_KEY_PARAM_NAME
from consts.report_consts import (
    REPORT_KEY_NAME,
    PERMITTED_REPORTS,
    NET_GAIN_LOSS,
    RECOMMENDED_INVESTMENTS,
)
from web_drivers.HLDriver import HLDriver
from web_drivers.util.HLAuthInfo import HLAuthInfo


def get_env(variable_name: str) -> str:
    variable_value = os.getenv(variable_name)

    if variable_value is None:
        raise EnvironmentError(
            f"The environment variable {variable_name} was not found."
        )

    return variable_value


INVESTMENT_REC_NO = int(get_env("INVESTMENT_REC_NO"))
SNS_TOPIC_ARN = get_env("SNS_TOPIC_ARN")

notification_adapter = SNSAdapter()
param_adapter = SSMAdapter()

api_handler = SMAApiHandler(param_adapter.get_param(SSM_API_KEY_PARAM_NAME))
auth_info = HLAuthInfo(param_adapter)
web_driver = HLDriver(auth_info)

notifier_app = HLInvestmentNotifier(
    api_handler, web_driver, notification_adapter, SNS_TOPIC_ARN
)


def handler(event, context):
    requested_report = event.get(REPORT_KEY_NAME)

    if requested_report not in PERMITTED_REPORTS:
        raise NotImplementedError("Requested report does not exist")

    if requested_report == NET_GAIN_LOSS:
        notifier_app.report_overall_gain_loss()

    elif requested_report == RECOMMENDED_INVESTMENTS:
        notifier_app.report_best_next_investments(INVESTMENT_REC_NO)

    return True
