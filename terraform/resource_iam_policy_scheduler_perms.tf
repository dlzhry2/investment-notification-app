resource "aws_iam_policy" "scheduler_further_perms" {
  name        = "scheduler_further_perms"
  path        = "/"
  description = "IAM policy for the scheduler permissions"
  policy      = data.aws_iam_policy_document.scheduler_perms.json
}
