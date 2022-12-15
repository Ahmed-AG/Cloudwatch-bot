import boto3
import time
import json
import openai
import sys
import os

def get_openAIKey():
    return os.environ['OPENAI_API_KEY']

def get_query(human_request):
    openai.api_key = get_openAIKey()
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt=generate_prompt(animal),
        prompt=human_request,
        temperature=0.6,
    )
    return response

if __name__ == "__main__":
    human_request = sys.argv[1]

    # Get Cloudwatch insights client
    insights_client = boto3.client('logs')
    
    # Define the query and Log Group Name
    # query = 'fields @timestamp, sourceIPAddress, eventName | sort @timestamp desc | limit 20'
    query = get_query(human_request)
    print(query['choices'][0]['text'][2:])
    exit()


    # # logGroupName = "CloudTrailLogs"
    # logGroupName = event['log_group_name']

    # # Execute the query
    # start_query_response = insights_client.start_query(
    #     logGroupNames=[
    #         logGroupName,
    #     ],
    #     startTime=1670457600,
    #     endTime=1670543999,
    #     queryString=query,
    #     # limit=123
    # )
    # time.sleep(10)
    # print(start_query_response['queryId'])

    # response = insights_client.get_query_results(
    #     queryId=start_query_response['queryId']
    # )
        
    # # Return the list as a JSON string
    # print(response)