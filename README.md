# Cloudwatch-bot

## use

1. Make sure that you have cloudtrail enabled. If not use `templates/logsinsight-bot.yaml` to enable cloudtrail and create a loggroup
2. set your envinroment with the following three parameters
```bash
export OPENAI_API_KEY=<Open AI Key>
export AWS_DEFAULT_REGION=<Region>
export LOGGROUP_NAME=<Cloud Trail LogGroup to search>
```
3. Run cloudwatch-bot with a natural laguage question as a parameter
```bash
python3 bin/cloudwatch-bot.py "show me the event name, ip address and arn witha limit of 7 ->"
```