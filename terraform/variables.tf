variable "account_holder_name" {
  default     = "Daniel"
  description = "The name of the account holder. This is used in the SNS Topic Name"
  type        = string
}

variable "investment_notifier_lambda_function_name" {
  default = "investmentNotifierLambda"
  type    = string
}

variable "main_user_email" {
  default     = "FILL_ME_IN"
  description = "Email address for the primary recipient of investment notifications. Any new users can be added manually."
  type        = string
  validation {
    condition     = can(regex("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", var.main_user_email))
    error_message = "Please provide a valid email address."
  }
}

variable "param_name_placeholder" {
  default     = "FILL_ME_IN"
  description = "The default placeholder text for an SSM parameter"
  type        = string
}

variable "ecr_source_repo_name" {
  default     = "FILL_ME_IN"
  description = "The name of the ECR repository containing your investment notifier app image"
  type        = string
}
