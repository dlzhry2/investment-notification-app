terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-2"
}

resource "aws_lambda_function" "investment_notifier_lambda" {
  function_name = var.investment_notifier_lambda_function_name
  package_type  = "Image"
  timeout       = 20
  memory_size   = 1024
  role          = aws_iam_role.notifier_lambda_role.arn
  image_uri     = "${data.aws_ecr_repository.source_repo.repository_url}:latest"

  environment {
    variables = {
      INVESTMENT_REC_NO = 5,
      SMA_BASE_URL      = "https://www.alphavantage.co/",
      SNS_TOPIC_ARN     = aws_sns_topic.investment_notifications.arn
    }
  }
}
