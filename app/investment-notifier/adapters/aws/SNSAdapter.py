import boto3
from adapters.BaseNotificationAdapter import BaseNotificationAdapter


class SNSAdapter(BaseNotificationAdapter):
    def __init__(self):
        self.client = boto3.client("sns")

    def notify(self, topic: str, message: str) -> None:
        self.client.publish(
            TopicArn=topic,
            Message=message
        )
