import json
import base64

# noinspection PyUnresolvedReferences
import boto3


# noinspection PyUnusedLocal
def lambda_handler(event, context):
    try:
        s3_client = boto3.client("s3")

        file_content = event["file_content"]
        file_name = event["file_name"]
        bucket_name = event["bucket_name"]

        if not file_content or not file_name or not bucket_name:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {
                        "message": "file_content, file_name, and bucket_name are required."
                    }
                ),
            }

        decoded_file_content = base64.b64decode(file_content)

        s3_client.put_object(
            Bucket=bucket_name, Key=file_name, Body=decoded_file_content
        )

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": f"File {file_name} uploaded successfully to bucket {bucket_name}."
                }
            ),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "message": "An error occurred while uploading the file.",
                    "error": str(e),
                }
            ),
        }
