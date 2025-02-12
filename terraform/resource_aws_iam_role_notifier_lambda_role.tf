resource "aws_iam_role" "notifier_lambda_role" {
  name               = "notifier_lambda_role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role.json
}
