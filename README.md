# A Lambda CI/CD Workflow on AWS to support a Python REST endpoint

## About The Endpoint
The Endpoint is written in Python and includes unit tests.  It is deployed to AWS environment(s) in the form of a Lambda that is triggered from API Gateway.  All of the code and infrastructure as code lives in this Repo.  

## CI/CD Pipeline
CodePipeline is used to manage all of the stages and steps in the CI/CD workflow which includes all of the steps including manual approvals involved in moving the code into production.  It uses CodeBuild to run the unit tests.  All Code is in Cloudformation (SAM).  Pushing both the Endpoint code or iac code into the master branch will kick off the pipeline.

## Usage  
Developers of the lambda can test their Python REST Endpoint locally and once they are satisfied with it, they need push the code into their master branch in this repository.  The push of the code triggers the pipeline including all steps to deploy the lambda.
