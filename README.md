# Cloudwatch-bot
## Set Up
1. Setting up Needed AWS Infrastrucure: Make sure that you have cloudtrail enabled and a Cloudwatch Log Group os created. You can use `templates/logsinsight-bot.yaml` to enable cloudtrail and create a loggroup
2. Sign up to OpenAI at https://openai.com and create an API Key

## Tuning your own model
OpenAI allows you to tune your own versions of their model. for example you can tune the default davinci model on a specific use case

To do that:
1. Create your sample tunning JSONL file with few hundreds examples
Example:
```
{"prompt":"Show me the fields eventName, eventSource, source IP, with a limit of 79 ->","completion":" fields @timestamp, eventName, eventSource, sourceIPAddress | sort @timestamp desc | limit 79 ###"}
```
2. Create your tuned model
```bash
openai api fine_tunes.create -t <tuning-file>.jsonl -m davinci --suffix <Personal Identifier>
```

3. Update the code to use your newly created model instead of the default `text-davinci-003`
```
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

```
## Use

2. set your envinroment with the following three parameters
```bash
export OPENAI_API_KEY=<Open AI Key>
export AWS_DEFAULT_REGION=<Region>
export LOGGROUP_NAME=<Cloud Trail LogGroup to search>
```
3. Run cloudwatch-bot with a natural laguage question as a parameter
```bash
python3 bin/cloudwatch-bot.py <Questions>
```

Examples
```bash
python3 bin/cloudwatch-bot.py "show me the event name, ip address and arn with a limit of 7 ->"
```