data "aws_iam_policy_document" "lambda_further_perms" {
  # Cloudwatch permissions
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]

    resources = ["arn:aws:logs:*:*:*"]
  }

  # SNS permissions
  statement {
    effect = "Allow"

    actions = [
      "sns:Publish"
    ]

    resources = [resource.aws_sns_topic.investment_notifications.arn]
  }

  # SSM permissions
  statement {
    effect = "Allow"

    actions = [
      "ssm:GetParameter"
    ]

    resources = ["*"]
  }

  # KMS permissions
  statement {
    effect = "Allow"

    actions = [
      "kms:Decrypt"
    ]

    resources = ["*"]
  }
}
