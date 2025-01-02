import logging
import json

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Log the received event
        logger.info(f"Received event: {json.dumps(event)}")
        
        return {"statusCode": 200, "body": "Event processed successfully"}
    except Exception as e:
        logger.error(f"Error processing event: {e}")
        raise
