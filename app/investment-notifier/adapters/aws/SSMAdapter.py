import boto3


class SSMAdapter:
    def __init__(self):
        self.client = boto3.client("ssm")

    def get_param(self, param_name):
        return (
            self.client.get_parameter(Name=param_name, WithDecryption=True)
            .get("Parameter")
            .get("Value")
        )
