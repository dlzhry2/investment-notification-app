resource "aws_ssm_parameter" "hl_login_dob" {
  name  = "hl-login-dob"
  type  = "SecureString"
  value = var.param_name_placeholder

  lifecycle {
    ignore_changes = [value]
  }
}

resource "aws_ssm_parameter" "hl_login_password" {
  name  = "hl-login-password"
  type  = "SecureString"
  value = var.param_name_placeholder

  lifecycle {
    ignore_changes = [value]
  }
}

resource "aws_ssm_parameter" "hl_login_secure_no" {
  name  = "hl-login-secure-no"
  type  = "SecureString"
  value = var.param_name_placeholder

  lifecycle {
    ignore_changes = [value]
  }
}

resource "aws_ssm_parameter" "hl_login_username" {
  name  = "hl-login-username"
  type  = "SecureString"
  value = var.param_name_placeholder

  lifecycle {
    ignore_changes = [value]
  }
}

resource "aws_ssm_parameter" "sma_api_key" {
  name  = "sma-api-key"
  type  = "SecureString"
  value = var.param_name_placeholder

  lifecycle {
    ignore_changes = [value]
  }
}
