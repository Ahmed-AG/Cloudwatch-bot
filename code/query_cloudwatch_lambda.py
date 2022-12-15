import boto3
import time
import json
import openai
import sys
import os

def get_openAIKey(ssm_parameter_name):


    return os.environ['OPENAI_API_KEY']

def get_query(human_request, ssm_parameter_name):
    openai.api_key = get_openAIKey(ssm_parameter_name)
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt=generate_prompt(animal),
        prompt=human_request,
        temperature=0.6,
    )
    return response

def lambda_handler(event, context):
    ssm_parameter_name = event['ssm_parameter_name']
    human_request = event['human_request']
    # Get Cloudwatch insights client
    insights_client = boto3.client('logs')
    
    # Define the query and Log Group Name

    # query = 'fields @timestamp, sourceIPAddress, eventName | sort @timestamp desc | limit 20'
    query = get_query(human_request, ssm_parameter_name)
    return query

    # logGroupName = "CloudTrailLogs"
    logGroupName = event['log_group_name']

    # Execute the query
    start_query_response = insights_client.start_query(
        logGroupNames=[
            logGroupName,
        ],
        startTime=1670457600,
        endTime=1670543999,
        queryString=query,
        # limit=123
    )
    time.sleep(10)
    print(start_query_response['queryId'])

    response = insights_client.get_query_results(
        queryId=start_query_response['queryId']
    )
        
    # Return the list as a JSON string
    return response

print(get_query(sys.argv[1],0))