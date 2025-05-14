from adapters.BaseNotificationAdapter import BaseNotificationAdapter
from adapters.SMAApiHandler import SMAApiHandler
from services.sma_calculator import StockSMA
from web_drivers.WebDriver import WebDriver


class InvestmentNotifier:
    def __init__(
        self,
        sma_service: SMAApiHandler,
        investments_web_driver: WebDriver,
        notification_adapter: BaseNotificationAdapter,
        notification_endpoint: str,
    ):
        self.sma_service = sma_service
        self.investments_web_driver = investments_web_driver
        self.notification_adapter = notification_adapter
        self.notification_endpoint = notification_endpoint

    def report_best_next_investments(self) -> list[StockSMA]:
        raise NotImplementedError("Improper usage of InvestmentNotifier base class")

    def report_overall_gain_loss(self) -> str:
        raise NotImplementedError("Improper usage of InvestmentNotifier base class")
