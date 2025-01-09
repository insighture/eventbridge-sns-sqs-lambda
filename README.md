# EventBridge to SNS to SQS to Lambda - AWS SAM Application

## Overview

This AWS SAM application demonstrates a serverless pipeline that integrates the following AWS services:
1. **EventBridge**: Captures events and forwards them to an SNS topic.
2. **SNS**: Publishes the event to an SQS queue.
3. **SQS**: Queues the events for processing by a Lambda function.
4. **Lambda**: Processes the events and logs the output to **CloudWatch Logs**.

---

## Architecture Diagram

```
EventBridge -> SNS -> SQS -> Lambda -> CloudWatch Logs
```

---

## Prerequisites

- AWS CLI installed and configured.
- AWS SAM CLI installed.
- Python 3.13 installed.
- An AWS account with sufficient permissions to deploy serverless applications.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/eventbridge-sns-sqs-lambda.git
cd eventbridge-sns-sqs-lambda
```

### 2. Build the SAM Application
```bash
sam build
```

### 3. Deploy the SAM Application
Run the following command and follow the guided prompts to provide required stack details:
```bash
sam deploy --guided
```
This command will:
- Package the application.
- Deploy the stack to your AWS account.
- Generate the necessary resources.

### 4. Test the Application

1. **Manually Trigger an Event**:
   Use the AWS CLI to send a custom event to EventBridge:
   ```bash
   aws events put-events --entries '[
     {
       "Source": "custom.source",
       "DetailType": "TestEvent",
       "Detail": "{\"message\": \"Hello from EventBridge!\"}"
     }
   ]'
   ```

2. **Manually Trigger a Failed Event**:
   Use the AWS CLI to send a custom event to EventBridge:
   ```bash
   aws events put-events --entries '[
     {
       "Source": "custom.source",
       "DetailType": "TestEvent",
       "Detail": "{\"simulatedError\": \"true\"}"
     }
   ]'
   ```

3. **Verify Logs**:
   - Open the **CloudWatch Logs** console in AWS.
   - Navigate to the log group created by the Lambda function.
   - Confirm that the message is logged.

---

## Resources Created

- **EventBridge Rule**: Captures custom events with the source `custom.source`.
- **SNS Topic**: Publishes messages received from EventBridge.
- **SQS Queue**: Subscribes to the SNS Topic and queues messages.
- **Lambda Function**: Processes messages from the SQS Queue and logs them to CloudWatch Logs.

---

## Outputs

Upon deployment, the following outputs are available:

- **EventBridgeRuleArn**: The ARN of the EventBridge Rule.
- **SNSTopicArn**: The ARN of the SNS Topic.
- **SQSQueueUrl**: The URL of the SQS Queue.
- **LambdaFunctionName**: The name of the Lambda Function.

---

## Cleanup

To delete the resources created by this application:
```bash
sam delete
```

---

## Notes

- The Lambda function logs all received events to CloudWatch Logs for debugging and monitoring.
- Modify the `EventPattern` in the EventBridge rule to capture different events as needed.
- Ensure IAM policies are correctly configured for your environment to avoid permission issues.

---

## License

N/A

