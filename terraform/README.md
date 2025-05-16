# Terraform
The defined infrastructure for the investment notification project.

## How to run

```
terraform fmt
terraform plan -var="main_user_email={YOUR_EMAIL}" -var="account_holder_name={YOUR_NAME} -var="ecr_source_repo_name={YOUR_ECR_REPO}"
terraform apply -var="main_user_email={YOUR_EMAIL}" -var="account_holder_name={YOUR_NAME} -var="ecr_source_repo_name={YOUR_ECR_REPO}"
```

Finally, you will need to manually update each of the SSM parameters created by [resource_ssm_params](terraform/resource_ssm_params.tf)
to contain your secure HL login info and Alphavantage API key. They will default as "FILL_ME_IN" until you provide a value.
