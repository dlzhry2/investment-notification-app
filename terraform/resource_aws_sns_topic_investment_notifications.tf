resource "aws_sns_topic" "investment_notifications" {
  name         = "investment-notifications"
  display_name = "Daniel's Stock Feed"
}
