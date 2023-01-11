import boto3
import time
import json
import openai
import sys
import os
import time
from datetime import datetime, timedelta


def get_openAIKey():
    return os.environ['OPENAI_API_KEY']

def get_loggroupname():
    return os.environ['LOGGROUP_NAME']

def get_query(human_request):
    openai.api_key = get_openAIKey()
    response = openai.Completion.create(
        # model="text-davinci-003",
        model="davinci:ft-personal:aag-cloudwatch-2023-01-03-18-19-47",
        stop="###",
        prompt=human_request,
        temperature=0,
        max_tokens=250,
    )
    print("OpenAI Query: " + response['choices'][0]['text'])
    return response['choices'][0]['text']

def read_logs(query, Loggroupname):
    insights_client = boto3.client('logs')
    
    current_epoch_time = int(time.time())
    subtraction_amount = timedelta(days=10)
    new_epoch_time = current_epoch_time - int(subtraction_amount.total_seconds())

    # print(current_epoch_time)
    # print(new_epoch_time)
    start_query_response = insights_client.start_query(
        logGroupNames=[
            logGroupName,
        ],
        startTime=new_epoch_time,
        endTime=current_epoch_time,
        queryString=query,
        # limit=123
    )
    time.sleep(10)

    response = insights_client.get_query_results(
        queryId=start_query_response['queryId']
    )
    return response

def parse_json_to_csv(response):
    query_results_csv = ""
    for result in response['results']:
        for field in result:
            if field['field'] != '@ptr': 
                query_results_csv = query_results_csv + field['value'] + ","
        query_results_csv = query_results_csv[:-1] + "\n"
    return query_results_csv

def parse_json_to_tab(response):
    query_results_csv = ""
    for result in response['results']:
        for field in result:
            if field['field'] != '@ptr': 
                query_results_csv = query_results_csv + field['value'] + "\t"
        query_results_csv = query_results_csv[:-1] + "\n"
    return query_results_csv

if __name__ == "__main__":
    human_request = sys.argv[1]
    # print(time.time())
    # # subtraction_amount = timedelta(days=10)
    # # new_epoch_time = time.time() - subtraction_amount.total_seconds()
    # # print(new_epoch_time)
    # exit()
    # Define the query and Log Group Name
    # query = 'fields @timestamp, userIdentity.arn, sourceIPAddress, eventName | sort @timestamp desc | limit 20'
    # query = '\n\nfields @timestamp | sort @timestamp desc | limit 200'

    query = get_query(human_request)

    logGroupName = get_loggroupname()
    response = read_logs(query, logGroupName)
    response_csv = parse_json_to_csv(response)
    response_tab = parse_json_to_tab(response)
    # print(json.dumps(response)) 
    print(response_tab)