# investment-notification-app
Anpplication to report pertinent information on your assets such as daily change (%) or recommending your best next investment.

## Why?
It has been built as a generic application, which could easily be extended to support interacting with other investment platforms.

But the main driver behind this app was that the HL Platform does not offer an API for customers.

## What
The application will provide updates every 2 days on your overall portfolio gain/loss (%) and at the end of the month, it provides a report with your top X investments based on 200-day SMA.

## How to run
### pre-requisites
- Hargreaves Lansdown investment account
- Python 3.12 (if you want to run quality checks)
- Docker
- AWS Account and AWS CLI
- API key for your free [Alphavantage](https://www.alphavantage.co/) account

```
Create a private ECR repository in your AWS account
Navigate to the new ECR private repository and click "View push commands"
Carry out the instructions
(Doing so will build and tag the image defined in this repo and then push it to your account)

You may also want to tidy up after:
docker image ls
docker image rm {image_name}
```

Finally, navigate to the terraform directory and follow the instructions [there](terraform/README.md) to get the full stack deployed.
