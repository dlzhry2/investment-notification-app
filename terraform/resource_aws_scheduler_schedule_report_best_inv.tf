resource "aws_scheduler_schedule" "report_best_inv" {
  name        = "report-best-investment-options"
  description = "Prompt lambda to recommend investments at the end of the month"

  flexible_time_window {
    mode                      = "FLEXIBLE"
    maximum_window_in_minutes = 5
  }

  target {
    arn      = aws_lambda_function.investment_notifier_lambda.arn
    role_arn = aws_iam_role.scheduler_role.arn

    input = jsonencode({
      report = "recommended investments"
    })

    retry_policy {
      maximum_retry_attempts       = 5
      maximum_event_age_in_seconds = 6000
    }
  }

  schedule_expression          = "cron(00 17 28 * ? *)"
  schedule_expression_timezone = "Europe/London"
}
