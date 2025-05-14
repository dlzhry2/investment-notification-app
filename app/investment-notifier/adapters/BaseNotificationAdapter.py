class BaseNotificationAdapter:
    def notify(self, topic: str, message: str) -> None:
        raise NotImplementedError
