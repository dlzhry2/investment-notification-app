data "aws_iam_policy_document" "scheduler_perms" {
  # Lambda permissions
  statement {
    effect = "Allow"

    actions = [
      "lambda:InvokeFunction",
    ]

    resources = [aws_lambda_function.investment_notifier_lambda.arn]
  }
}
