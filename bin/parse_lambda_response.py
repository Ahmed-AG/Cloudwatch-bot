import json
import sys

def read_lambda_response(response_file):
    File_object = open(response_file, "r")
    response = json.loads(File_object.read())
    return response

def parse_json_to_csv(response):
    query_results_csv = ""
    for result in response['results']:
        for field in result:
            query_results_csv = query_results_csv + field['value'] + ","
        query_results_csv = query_results_csv[:-1] + "\n"
    return query_results_csv

def parse_json_to_tab(response):
    query_results_csv = ""
    for result in response['results']:
        for field in result:
            query_results_csv = query_results_csv + field['value'] + "\t"
        query_results_csv = query_results_csv[:-1] + "\n"
    return query_results_csv

response_file = sys.argv[1]
lambda_response = read_lambda_response(response_file)
lambda_response_csv = parse_json_to_csv(lambda_response)
lambda_response_tab = parse_json_to_tab(lambda_response)

print(lambda_response_tab)