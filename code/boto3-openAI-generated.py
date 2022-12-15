import boto3
import json

def lambda_handler(event, context):
    # Get Cloudwatch insights client
    insights_client = boto3.client('cloudwatch')
    
    # Define the query
    query = 'fields @timestamp, @message | sort @timestamp desc | limit 20'
    
    # Execute the query
    response = insights_client.query(
        QueryString = query
    )
    
    # Create a list of dictionaries from the query results
    query_results = response['Results']
    results_list = []
    for result in query_results:
        results_list.append(dict(result))
    
    # Return the list as a JSON string
    return {
        'statusCode': 200,
        'body': json.dumps(results_list)
    }