# Mini-Project: Automation For The People!

This mini-project is an application that exposes a Rest Endpoint which returns a JSON payload displaying a generic message and current time. It includes source code, infrastructure (IaC) code and unit tests.  Push your code to the master branch of this repo and it will trigger the build, test, manual approval, and deployment of your endpoint.  After successful deployment, the endpoint is accessible via the API gateway Invoke URL.  You can perform 2 actions, a GET on the URL which will display a generic message or a POST which returns a response echoing the message you posted in the body of your POST request.  

The source code was developed with Python and the IaC was defined in Cloudformation and Serverless Application Model (SAM).  This is a mostly AWS solution except that GitHub was used instead of CodeCommit.  The AWS managed services include:
* **Lambda** to process the requests events via **API Gateway**
* **CodePipeline** to manage getting the code through all the steps and stages on its way to deployment (including webhook)
* **Secrets Manager** to manage the GitHub secret used in the webhook (and referenced in the CloudFormation template)
* **CodeBuild** to run the unit tests and package the Lambda in an **S3** bucket
* **SNS** to send a notification when the manual approval is needed in the pipeline
* **IaM** to create all of the roles necessary in the pipeline.  

## Getting Started

These instructions guide you through the prerequisites steps and the recommended workflow for getting your endpoint up and running on AWS.

### Prerequisites

* Recommended Install SAM Local for faster feedback loop enabling you to test your lambda locally before deploying - https://aws.amazon.com/blogs/aws/new-aws-sam-local-beta-build-and-test-serverless-applications-locally/

* cd to the directory where requirements.txt is located, activate your virtualenv, and run:
```pip install -r requirements.txt```
in your shell to install all the python packages that are required.

* Set up a GITHUB webhook by creating a pipeline that has GITHUB as the source and connect.  You will only need to set up the webhook once and then you can use it in your lambda_workflow.yml Cloudformation template.  Also, remember the OAuthToken from this process and save it in SecretsManager.

* Modify the params.json file and tags.json file to include tags and parameters that are meaningful to you.  In particular, change the email address parameter in the params.json to be your email so that SNS messages related to the delivery pipeline will be emailed to you.

### Testing Locally

Test as much as of your code as you can locally before committing and pushing your code to master where it will kick off the pipeline using a GITHUB webhook.

The following commands can be used to validate your SAM template and test your lambda locally with the help of SAM Local:
```
sam validate
sam local start-api
curl -X GET http://127.0.0.1:3000/
curl -d '{"message": "Hello"}' -X POST http://127.0.0.1:3000/
echo '{"httpMethod": "GET"}' |sam local invoke "MessageProcessor"
echo '{"httpMethod": "POST", "body": "{\"message\": \"GREAT\"}"}' |sam local invoke "MessageProcessor"
```
The following commands can be used to run your unit tests locally:
```
python -m unittest discover
```

### Single Command deployment of your Lambda when you are ready

Run the following command to create your stack:
```
make create
```

### Code Pipeline
The make command (and pushing code to your master branch) will kick off your the CodePipeline which will:
* run your unit tests
* package your lambda
* prompt for manual approval to deploy
* deploy your lambda

### Accessing the live Endpoint
To access your endpoint, find the InvokeURL by going to Amazon Apigateway>Stages.  You can perform a get by simply clicking on the InvokeURL.  To echo a custom message, you will need to post a message in the following format to the InvokeURL:
```
{
  "message": "Your custom message here"
}
```

### CleanUp

Run the following command to clean up after yourself and remove all of the resources you created in AWS before you are charged extra.
```
make delete
```
The command will empty the contents of the s3 bucket so that your stack can successfully delete.  It also delets the SAM stack.
