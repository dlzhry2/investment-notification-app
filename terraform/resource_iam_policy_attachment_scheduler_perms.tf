resource "aws_iam_role_policy_attachment" "scheduler_further_perms" {
  role       = aws_iam_role.scheduler_role.name
  policy_arn = aws_iam_policy.scheduler_further_perms.arn
}
