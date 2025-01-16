# noinspection PyUnusedLocal
def lambda_handler(event, context):
    num1 = event["num1"]
    num2 = event["num2"]

    result = num1 + num2

    return {"result": result}
