resource "aws_sns_topic" "investment_notifications" {
  name         = "investment-notifications"
  display_name = "${var.account_holder_name}'s Stock Feed"
}
