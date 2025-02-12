resource "aws_iam_policy" "lambda_further_perms" {
  name        = "lambda_further_perms"
  path        = "/"
  description = "IAM policy for additional permissions"
  policy      = data.aws_iam_policy_document.lambda_further_perms.json
}
