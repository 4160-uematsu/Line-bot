import logging

import os
import urllib.request
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info(event)

    for message_event in json.loads(event["body"])["events"]:

        logger.info(json.dumps(message_event))

        url = "https://api.line.me/v2/bot/message/reply"

        headers = {
            "Content-Type": "application/json",
            'Authorization': 'Bearer ' + os.environ['ACCESSTOKEN']
        }

        data = {
            "replyToken": message_event["replyToken"],
            "messages": [
                {
                    "type": "text",
                    "text": message_event["message"]["text"],
                }
            ]
        }

        req = urllib.request.Request(url=url, data=json.dumps(data).encode("utf-8"), method="POST", headers=headers)

        with urllib.request.urlopen(req) as res:

            logger.info(res.read().decode("utf-8"))

            return {
                "statusCode": 200,
                "body": json.dumps("Hello from Lambda!")
            }