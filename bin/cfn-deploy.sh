#!/bin/bash

aws cloudformation deploy --template-file $TEMPLATE_FILE \
    --stack-name $STACK_NAME \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
    --region $REGION
    # --parameter-overrides Key1=Value1 Key2=Value2 --tags Key1=Value1 Key2=Value2
