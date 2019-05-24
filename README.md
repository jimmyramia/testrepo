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

* Install SAM Local - https://aws.amazon.com/blogs/aws/new-aws-sam-local-beta-build-and-test-serverless-applications-locally/

* cd to the directory where requirements.txt is located, activate your virtualenv, and run:
```pip install -r requirements.txt```
in your shell to install all the python packages that are required.

* Set up a GITHUB webhook by creating a pipeline that has GITHUB as the source and connect.  You will only need to set up the webhook once and then you can use it in your lambda_workflow.yml Cloudformation template.  Also, remember the OAuthToken from this process and save it in SecretsManager.

* Modify the params.json file and tags.json file to include tags and parameters that are meaningful to you.  In particular, change the email address parameter in the params.json to be your email so that SNS messages related to the delivery pipeline will be emailed to you.

### CI/CD Workflow

The workflow starts with local testing so it is suggested that you use SAM Local so you can do most of your lambda testing locally.  To get started with SAM Local, view the instructions here:

Once you have SAM local installed, you can run the following commands to run the server

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## CleanUp

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
