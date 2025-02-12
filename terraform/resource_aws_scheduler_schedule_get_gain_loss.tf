resource "aws_scheduler_schedule" "get_gain_loss" {
  name        = "get-gain-loss"
  description = "Reports the gain/loss"

  flexible_time_window {
    mode                      = "FLEXIBLE"
    maximum_window_in_minutes = 5
  }

  target {
    arn      = aws_lambda_function.investment_notifier_lambda.arn
    role_arn = aws_iam_role.scheduler_role.arn

    input = jsonencode({
      report = "net gain/loss"
    })

    retry_policy {
      maximum_retry_attempts       = 5
      maximum_event_age_in_seconds = 6000
    }
  }

  schedule_expression          = "cron(30 16 ? * 2,4,6 *)"
  schedule_expression_timezone = "Europe/London"
}
