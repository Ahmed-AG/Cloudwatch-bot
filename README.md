# Cloudwatch-bot
## Set Up
### Setting up Needed AWS Infrastrucure
Make sure that you have cloudtrail enabled. If not use `templates/logsinsight-bot.yaml` to enable cloudtrail and create a loggroup
### Creating OpenAI Account and getting an API Key
Sign up to OpenAI

## Tuning your own model
### training Set
Tuning file
### Creating the personal model
```bash
openai api fine_tunes.create -t <tuning-file>.jsonl -m davinci --suffix <Personal Identifier>
```

## use

2. set your envinroment with the following three parameters
```bash
export OPENAI_API_KEY=<Open AI Key>
export AWS_DEFAULT_REGION=<Region>
export LOGGROUP_NAME=<Cloud Trail LogGroup to search>
```
3. Run cloudwatch-bot with a natural laguage question as a parameter
```bash
python3 bin/cloudwatch-bot.py "Questions ->"
```

Examples