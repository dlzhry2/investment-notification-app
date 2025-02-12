output "investment_notifier_function_arn" {
  value = aws_lambda_function.investment_notifier_lambda.arn
}

output "gain_loss_schedule_arn" {
  value = aws_scheduler_schedule.get_gain_loss.arn
}

output "best_investment_schedule_arn" {
  value = aws_scheduler_schedule.report_best_inv.arn
}

output "sns_topic_arn" {
  value = aws_sns_topic.investment_notifications.arn
}
