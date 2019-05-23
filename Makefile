STACK:=restapi-workflow-stack
TEMPLATE:=lambda_workflow.yml
PARAMETERS:=params.json
TAGS:=tags.json
BUCKET:=mysandbox-ramiaj-lambda-bucket

create:
	aws cloudformation create-stack --stack-name $(STACK) --template-body file://`pwd`/$(TEMPLATE) --parameters file://`pwd`/$(PARAMETERS) --tags file://`pwd`/$(TAGS) --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND

update:
	aws cloudformation update-stack --stack-name $(STACK) --template-body file://`pwd`/$(TEMPLATE) --parameters file://`pwd`/$(PARAMETERS) --tags file://`pwd`/$(TAGS) --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND

delete:
	python3 remove_bucket_contents.py $(BUCKET)
	aws cloudformation delete-stack --stack-name $(STACK)
