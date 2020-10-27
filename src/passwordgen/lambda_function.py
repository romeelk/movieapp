import json
import random
import string


def lambda_handler(event, context):

    print(event)
    number = int(event['number'])
    if number == 0:
        return response(400, "Invalid request:number key must be integer val between 8,10")

    password = password_gen(number)

    return response(200, password)


def password_gen(number):
    letters = string.ascii_lowercase
    password = ''.join(random.sample(letters, number))
    return password


def response(response_code, value):
    return {
        'statusCode': response_code,
        'body': json.dumps(value)
    }

