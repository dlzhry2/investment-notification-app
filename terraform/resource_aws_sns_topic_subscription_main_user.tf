resource "aws_sns_topic_subscription" "main_user" {
  topic_arn = aws_sns_topic.investment_notifications.arn
  protocol  = "email"
  endpoint  = var.main_user_email
}
