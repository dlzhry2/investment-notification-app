resource "aws_cloudwatch_log_group" "invement_notifier" {
  name              = "/aws/lambda/${var.investment_notifier_lambda_function_name}"
  retention_in_days = 14
}
