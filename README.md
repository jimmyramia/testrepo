# Mini-Project: An application that exposes a Rest Endpoint which returns a JSON payload displaying a generic message and current time.  

This mini-project includes source code, infrastructure (IaC) code and unit tests.  Simply push your code to the master branch of this repo and it will trigger the build, test, manual approval, and deployment of your endpoint.  After successful deployment, the endpoint is accessible via the API gateway Invoke URL.  You can perform 2 actions, a GET on the URL which will display a generic message or a POST to the invoke URL which will echo the message you posted in the body of your request.  

The source code was developed with Python and the IaC was defined in Cloudformation and Serverless Application Model (SAM).  This is a 100% AWS solution including using Lambda to process the requests made via API gateway, CodePipeline to manage getting the code through all the steps and stages on its way to deployment, CodeBuild to run the unit tests and package the Lambda in an S3 bucket, SNS to send a notification when the manual approval is needed in the pipeline, and IaM to create all of the roles necessary in the pipeline.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

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
