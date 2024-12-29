"""Class to emulate actual notifier classes. Locally will simply print the message."""
from adapters.BaseNotificationAdapter import BaseNotificationAdapter

class LocalNotificationAdapter(BaseNotificationAdapter):
    def notify(self, topic: str, message: str) -> None:
        print(f"Notifiying subscribed parties. Topic: {topic}...")
        print(f"Message: {message}")
