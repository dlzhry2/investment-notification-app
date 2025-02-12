resource "aws_iam_role" "scheduler_role" {
  name               = "scheduler_role"
  assume_role_policy = data.aws_iam_policy_document.scheduler_assume_role.json
}
