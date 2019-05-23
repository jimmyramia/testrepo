sam validate
sam local start-api
curl -X GET http://127.0.0.1:3000/
curl -d '{"message": "Hello"}' -X POST http://127.0.0.1:3000/
-OR-
echo '{"httpMethod": "GET"}' |sam local invoke "MessageProcessor"
echo '{"httpMethod": "POST", "body": "{\"message\": \"GREAT\"}"}' |sam local invoke "MessageProcessor"

codebuild:

aws cloudformation package --template-file template.yml --s3-bucket mysandbox-ramiaj-lambdabucket --output-template-file packaged.yml

aws s3 mb s3://mysandbox-ramiaj-lambdabucket

aws cloudformation create-stack --stack-name restapi-workflow-stack --template-body file://./lambda_workflow.yml --parameters file://./params.json --tags file://./tags.json --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
aws cloudformation delete-stack --stack-name restapi-workflow-stack
aws cloudformation update-stack --stack-name restapi-workflow-stack --template-body file://./lambda_workflow.yml --parameters file://./params.json --tags file://./tags.json --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM

python3 remove_bucket_contents.py mysandbox-ramiaj-lambda-bucket
