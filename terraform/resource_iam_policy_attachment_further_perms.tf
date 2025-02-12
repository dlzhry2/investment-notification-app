resource "aws_iam_role_policy_attachment" "lambda_further_perms" {
  role       = aws_iam_role.notifier_lambda_role.name
  policy_arn = aws_iam_policy.lambda_further_perms.arn
}
