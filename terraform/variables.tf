variable "env_name_placeholder" {
  # TODO - replace with SSM in next PR
  default     = "FILL_ME_IN"
  description = "The default placeholder text for a lambda environment variable"
  type        = string
}

variable "main_user_email" {
  default     = "FILL_ME_IN"
  description = "My email address. Any new users can be added manually."
  type        = string
  validation {
    condition     = can(regex("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", var.main_user_email))
    error_message = "Please provide a valid email address."
  }
}

variable "investment_notifier_lambda_function_name" {
  default = "investmentNotifierLambda"
  type    = string
}
