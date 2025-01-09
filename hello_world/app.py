import logging
import json
import time

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            # Parse the outer SQS message
            sqs_body = json.loads(record['body'])
            
            # Parse the SNS message
            sns_message = json.loads(sqs_body['Message'])
            
            # Extract the "detail" field in the SNS message
            event_detail = sns_message.get('detail', {})

            # Extract the timestamp from the message (if available)
            start_time = float(sqs_body.get('timestamp', time.time() * 1000))
            current_time = time.time() * 1000
            latency = current_time - start_time
 
            # Log latency
            logger.info(f"Event Latency: {latency} ms")

            # Log full event
            logger.info(f"Processing message: {json.dumps(sqs_body)}")

            # Simulate failure for certain statuses
            status = event_detail.get('status', '')
            if status != "success":
                raise ValueError(f"Unexpected status: {status}")
            
        
        return {"statusCode": 200, "body": "Messages processed successfully"}
    except Exception as e:
        logger.error(f"Error processing event: {e}")
        raise
