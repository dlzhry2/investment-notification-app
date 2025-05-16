data "aws_ecr_repository" "source_repo" {
  name = var.ecr_source_repo_name
}
