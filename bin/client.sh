#!/bin/bash

# Setting variables
function_name=$(aws cloudformation describe-stack-resources --stack-name $STACK_NAME --region $REGION | jq -r '.StackResources[] | select(.ResourceType|IN("AWS::Lambda::Function")) | .PhysicalResourceId')
log_group_name=$(aws cloudformation describe-stack-resources --stack-name $STACK_NAME --region $REGION | jq -r '.StackResources[] | select(.ResourceType|IN("AWS::Logs::LogGroup")) | .PhysicalResourceId')
ssm_parameter_name=$(aws cloudformation describe-stack-resources --stack-name $STACK_NAME --region $REGION | jq -r '.StackResources[] | select(.ResourceType|IN("AWS::SSM::Parameter")) | .PhysicalResourceId')

# Fetching query
human_request=$1

payload='{"log_group_name": "'$log_group_name'", "human_request": "'$human_request'", "ssm_parameter_name": "'$ssm_parameter_name'"}'

# Invoke LogsInsight-bot
aws lambda invoke --function-name $function_name \
    --cli-binary-format raw-in-base64-out \
    --payload "$payload" \
    --region $REGION $LAMBDA_OUTPUT_FILE

# Parse lambda response into CSV
# python3 bin/parse_lambda_response.py $LAMBDA_OUTPUT_FILE