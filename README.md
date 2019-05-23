# A Lambda CI/CD Workflow on AWS to support a Python REST endpoint

## About The Endpoint
The Endpoint is written in Python and includes unit test of the get method.  It is deployed to AWS environment as a Lambda that is triggered from API Gateway.  All of the code and infrastructure as code lives in this repo.  

## CI/CD Pipeline
CodePipeline is used to manage all of the stages and steps in the CI/CD workflow which includes manual approvals before deployment.  It uses CodeBuild to run the unit tests.  Lambda Is Configured in Cloudformation (SAM) and the rest of the IAC is in a standard Cloudformation template.  Pushing any code into the master branch in this repo will recreate the Lambda and infrastructure.

## Usage  
Developers of the lambda can test their Python REST Endpoint locally and once they are satisfied with it, they need push the code into their master branch in this repository.  The push of the code triggers the pipeline including all steps to deploy the lambda.
