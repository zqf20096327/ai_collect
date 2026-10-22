<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/aws.png">
</p>
<br/>

# Awesome AWS [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome AWS libraries, open source repos, guides, blogs, and other resources.

Inspired by the <b><code>522448⭐</code></b> <b><code>&nbsp;37619🍴</code></b> [awesome](https://github.com/sindresorhus/awesome)) list.

## The Fiery Meter of AWSome

* Repo with 0100+ Stars: :fire:
* Repo with 0200+ Stars: :fire::fire:
* Repo with 0500+ Stars: :fire::fire::fire:
* Repo with 1000+ Stars: :fire::fire::fire::fire:
* Repo with 2000+ Stars: :fire::fire::fire::fire::fire:

Repos not on `The Fiery Meter of AWSome` can still be awesome, see [A Note on Repo AWSomeness](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md#a-note-on-repo-awsomeness).

### `awesome-aws` Python Module

[![Build Status](https://travis-ci.org/donnemartin/awesome-aws.svg?branch=master)](https://travis-ci.org/donnemartin/awesome-aws) [![Codecov](https://img.shields.io/codecov/c/github/donnemartin/awesome-aws.svg)](https://codecov.io/github/donnemartin/awesome-aws) [![PyPI version](https://badge.fury.io/py/awesome-aws.svg)](http://badge.fury.io/py/awesome-aws)

The Python module [`awesome-aws`](https://github.com/correia-jpv/fucking-awesome-aws/tree/master/awesome) regularly scans repos on [Awesome AWS](https://github.com/correia-jpv/fucking-awesome-aws) to maintain the accuracy of the `Fiery Meter of AWSome`.

## Contributing

Contributions are welcome!

Review the [Contributing Guidelines](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md).

Also check out the [Watch List](https://github.com/correia-jpv/fucking-awesome-aws/issues/34).

## Index

* [SDKs and Samples](#sdks-and-samples)
    * [Android](#android-sdk)
    * [C++](#c-sdk)
    * [Clojure](#clojure-sdk)
    * [Go](#go-sdk)
    * [iOS](#ios-sdk)
    * [IoT](#iot-sdk)
    * [Java](#java-sdk)
    * [JavaScript](#javascript-sdk)
    * [Haskell](#haskell-sdk)
    * [Perl](#perl-sdk)
    * [PHP](#php-sdk)
    * [Python](#python-sdk)
    * [Ruby](#ruby-sdk)
    * [Rust](#rust-sdk)
    * [Scala](#scala-sdk)
    * [Xamarin](#xamarin-sdk)
    * [Unity](#unity-sdk)
    * [.NET](#net-sdk)
* [Command Line Tools](#command-line-tools)
    * [Universal Command Line Interface](#universal-command-line-interface)
    * [Windows PowerShell](#windows-powershell)
* [IDE Toolkits](#ide-toolkits)
    * [Eclipse Toolkit](#eclipse-toolkit)
    * [Visual Studio Toolkit](#visual-studio-toolkit)
* [Open Source Repos](#open-source-repos)
    * [API Gateway](#api-gateway)
    * [CLI](#cli)
    * [CloudFormation](#cloudformation)
    * [CloudSearch](#cloudsearch)
    * [CloudTrail](#cloudtrail)
    * [CloudWatch](#cloudwatch)
    * [Code Deploy](#code-deploy)
    * [Code Pipeline](#code-pipeline)
    * [Cognito](#cognito)
    * [Data Pipeline](#data-pipeline)
    * [Device Farm](#device-farm)
    * [DynamoDB](#dynamodb)
    * [Elastic Beanstalk](#elastic-beanstalk)
    * [Elastic Container Service](#elastic-container-service)
    * [Elastic File System](#elastic-file-system)
    * [Elastic MapReduce](#elastic-mapreduce)
    * [Elastic Search](#elastic-search)
    * [Elasticache](#elasticache)
    * [Glacier](#glacier)
    * [Kinesis](#kinesis)
    * [Lambda](#lambda)
    * [Machine Learning](#machine-learning)
    * [Mobile Analytics](#mobile-analytics)
    * [OpsWorks](#opsworks)
    * [Redshift](#redshift)
    * [Route 53](#route-53)
    * [S3](#s3)
    * [SNS](#sns)
    * [SQS](#sqs)
    * [Data](#data)
    * [DevOps](#devops)
    * [Security](#security)
    * [Accompanying](#accompanying-repos)
    * [Miscellaneous](#miscellaneous-repos)
* [Guides, Books, Documentation, and Training](#guides-books-documentation-and-training)
    * [Getting Started Guides](#getting-started-guides)
    * [General Guides](#general-guides)
    * [Books](#books)
    * [Whitepapers](#whitepapers)
    * [Documentation](#documentation)
    * [Training](#training)
    * [Case Studies: Powered by AWS](#case-studies-powered-by-aws)
* [Social](#social)
    * [Blogs](#blogs)
    * [Twitter Influencers](#twitter-influencers)
    * [Facebook Pages](#facebook-pages)
    * [YouTube Channels](#youtube-channels)
    * [LinkedIn Groups](#linkedin-groups)
    * [Subreddits](#subreddits)
    * [Conferences](#conferences)
* [Latest KPIs and Stats](#latest-kpis-and-stats)
* [Appendix of Core Services](#appendix-of-core-services)
    * [Services in Plain English](#services-in-plain-english)
    * [Compute](#compute-services)
    * [Networking](#networking-services)
    * [Enterprise Applications](#enterprise-applications)
    * [Analytics](#analytics-services)
    * [Artificial Intelligence](#artificial-intelligence)
    * [Management Tools](#management-tools)
    * [Security and Identity](#security-and-identity-services)
    * [Internet of Things](#internet-of-things-service)
    * [Mobile Services](#mobile-services)
    * [Storage and Content Delivery](#storage-and-content-delivery-services)
    * [Databases](#databases)
    * [Application Services](#application-services)
    * [Developer Tools](#developer-tools)
    * [Miscellaneous Services](#miscellaneous-services)
* [Contributing](#contributing)
* [Credits](#credits)
* [Other Awesome Lists](#other-awesome-lists)
* [Contact Info](#contact-info)
* [License](#license)

## SDKs and Samples

*AWS and community SDKs with samples and docs, grouped by language.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/TK96G8T.png">
</p>
<br/>

### Android SDK

* <b><code>&nbsp;&nbsp;1074⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;547🍴</code></b> [Repo :fire::fire::fire:](https://github.com/aws/aws-sdk-android))
* <b><code>&nbsp;&nbsp;1045⭐</code></b> <b><code>&nbsp;&nbsp;1028🍴</code></b> [Repo with Samples :fire::fire::fire:](https://github.com/awslabs/aws-sdk-android-samples))
* [Install](http://sdk-for-android.amazonwebservices.com/latest/aws-android-sdk.zip)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-android/)
* 🌎 [Learn More](aws.amazon.com/mobile/sdk/)

### C++ SDK

* <b><code>&nbsp;&nbsp;2214⭐</code></b> <b><code>&nbsp;&nbsp;1172🍴</code></b> [Repo :fire::fire::fire::fire:](https://github.com/awslabs/aws-sdk-cpp))
* 🌎 [Blog with Samples](aws.amazon.com/blogs/aws/introducing-the-aws-sdk-for-c/)

*The C++ SDK is a labs project with limited docs and/or samples.*

### Clojure SDK

* <b><code>&nbsp;&nbsp;1000⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;199🍴</code></b> [Repo :fire::fire::fire:](https://github.com/mcohen01/amazonica))
* <b><code>&nbsp;&nbsp;1000⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;199🍴</code></b> [Install](https://github.com/mcohen01/amazonica#installation))
* <b><code>&nbsp;&nbsp;1000⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;199🍴</code></b> [Docs](https://github.com/mcohen01/amazonica#documentation))

*The Clojure SDK is a community project with limited docs and/or samples.*)

### Go SDK

* <b><code>&nbsp;&nbsp;8662⭐</code></b> <b><code>&nbsp;&nbsp;2034🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-go))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [Install](https://github.com/aws/aws-sdk-go/wiki))
* [Docs](http://docs.aws.amazon.com/sdk-for-go/api/)
* 🌎 [Learn More](aws.amazon.com/sdk-for-go/)

Related Repos:

* <b><code>&nbsp;&nbsp;&nbsp;370⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;136🍴</code></b> [goamz/goamz :fire::fire:](https://github.com/goamz/goamz))

### iOS SDK

* <b><code>&nbsp;&nbsp;1704⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;897🍴</code></b> [Repo :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-ios))
* <b><code>&nbsp;&nbsp;1048⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;738🍴</code></b> [Repo with Samples :fire::fire::fire::fire:](https://github.com/awslabs/aws-sdk-ios-samples))
* [Install](http://sdk-for-ios.amazonwebservices.com/latest/aws-ios-sdk.zip)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-ios/)
* 🌎 [Learn More](aws.amazon.com/mobile/sdk/)

### IoT SDK

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;93⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;113🍴</code></b> [Repo for Arduino](https://github.com/awslabs/aws-sdk-arduino))
* <b><code>&nbsp;&nbsp;1062⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;634🍴</code></b> [Repo for C :fire::fire::fire:](https://github.com/aws/aws-iot-device-sdk-embedded-C))
* <b><code>&nbsp;&nbsp;&nbsp;965⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;375🍴</code></b> [Repo for JavaScript :fire::fire::fire:](https://github.com/aws/aws-iot-device-sdk-js))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [Repo for Arduino Yun :fire:](https://github.com/aws/aws-iot-device-sdk-arduino-yun/))
* [Docs](http://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

*The IoT SDK is a labs project with limited docs and/or samples.*

### Java SDK

* <b><code>&nbsp;&nbsp;4203⭐</code></b> <b><code>&nbsp;&nbsp;2774🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-java))
* <b><code>&nbsp;&nbsp;&nbsp;241⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;357🍴</code></b> [Repo with Samples :fire::fire:](https://github.com/awslabs/aws-java-sample))
* [Install](http://sdk-for-java.amazonwebservices.com/latest/aws-java-sdk.zip)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-java/)
* 🌎 [Learn More](aws.amazon.com/sdk-for-java/)

### JavaScript SDK

* <b><code>&nbsp;&nbsp;7600⭐</code></b> <b><code>&nbsp;&nbsp;1518🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-js))
* <b><code>&nbsp;&nbsp;&nbsp;306⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;170🍴</code></b> [Repo with Samples :fire::fire:](https://github.com/awslabs/aws-nodejs-sample))
* [Install](http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-intro.html)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-javascript/)
* 🌎 [Learn More](aws.amazon.com/sdk-for-node-js/)

Related Repos:

* <b><code>&nbsp;&nbsp;9554⭐</code></b> <b><code>&nbsp;&nbsp;2174🍴</code></b> [aws/aws-amplify :fire::fire::fire::fire::fire:](https://github.com/aws/aws-amplify))
* <b><code>&nbsp;&nbsp;&nbsp;457⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;50🍴</code></b> [chilts/awssum :fire::fire:](https://github.com/chilts/awssum))
* <b><code>&nbsp;&nbsp;&nbsp;681⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;165🍴</code></b> [mirkokiefer/aws-lib :fire::fire::fire:](https://github.com/mirkokiefer/aws-lib))
* <b><code>&nbsp;&nbsp;&nbsp;239⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;31🍴</code></b> [SaltwaterC/aws2js :fire::fire:](https://github.com/SaltwaterC/aws2js))

### Haskell SDK

* <b><code>&nbsp;&nbsp;&nbsp;615⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;250🍴</code></b> [Repo :fire::fire::fire:](https://github.com/brendanhay/amazonka))
* [Docs](http://hackage.haskell.org/packages/#cat:AWS)

Related Repos:

* <b><code>&nbsp;&nbsp;&nbsp;246⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;111🍴</code></b> [aristidb/aws :fire::fire:](https://github.com/aristidb/aws))

*The Haskell SDK is a community project with limited docs and/or samples.*

### Perl SDK

* <b><code>&nbsp;&nbsp;&nbsp;175⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;95🍴</code></b> [Repo :fire:](https://github.com/pplu/aws-sdk-perl))
* <b><code>&nbsp;&nbsp;&nbsp;175⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;95🍴</code></b> [Repo with Samples :fire:](https://github.com/pplu/aws-sdk-perl/tree/master/examples))
* <b><code>&nbsp;&nbsp;&nbsp;175⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;95🍴</code></b> [Install](https://github.com/pplu/aws-sdk-perl#installation))
* 🌎 [Docs](metacpan.org/pod/Paws)
* 🌎 [Learn More](metacpan.org/pod/Paws)

*The Perl SDK is a community project.*

### PHP SDK

* <b><code>&nbsp;&nbsp;6208⭐</code></b> <b><code>&nbsp;&nbsp;1253🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-php))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;88⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;72🍴</code></b> [Repo with Samples](https://github.com/awslabs/aws-php-sample))
* [Install](http://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-php/)
* 🌎 [Learn More](aws.amazon.com/sdk-for-php/)

Related Repos:

* <b><code>&nbsp;&nbsp;1714⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;242🍴</code></b> [aws-sdk-php-laravel :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-php-laravel))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;81⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;23🍴</code></b> [aws-sdk-php-silex](https://github.com/aws/aws-sdk-php-silex))
* <b><code>&nbsp;&nbsp;&nbsp;104⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;62🍴</code></b> [aws-sdk-php-zf2 :fire:](https://github.com/aws/aws-sdk-php-zf2))

### Python SDK

* <b><code>&nbsp;&nbsp;9918⭐</code></b> <b><code>&nbsp;&nbsp;1997🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/boto/boto3))
* <b><code>&nbsp;&nbsp;&nbsp;207⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;177🍴</code></b> [Repo with Samples :fire:](https://github.com/awslabs/aws-python-sample))
* [Install](http://github.com/boto/boto#installation)
* 🌎 [Docs](boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [Learn More](http://github.com/boto/boto/blob/develop/README.rst#boto)

Related Repos:

* <b><code>&nbsp;&nbsp;9918⭐</code></b> <b><code>&nbsp;&nbsp;1997🍴</code></b> [boto3 :fire::fire::fire::fire::fire:](https://github.com/boto/boto3))
* <b><code>&nbsp;&nbsp;1647⭐</code></b> <b><code>&nbsp;&nbsp;1192🍴</code></b> [botocore :fire::fire::fire::fire:](https://github.com/boto/botocore))

### Ruby SDK

* <b><code>&nbsp;&nbsp;3658⭐</code></b> <b><code>&nbsp;&nbsp;1232🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-ruby))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;32⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [Repo with S3 Sample](https://github.com/awslabs/aws-ruby-sample))
* [Install](http://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-install.html)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-ruby/)
* <b><code>&nbsp;10468⭐</code></b> <b><code>&nbsp;&nbsp;5837🍴</code></b> [Samples :fire::fire::fire::fire::fire:](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/ruby/example_code/))

Related Repos:

* <b><code>&nbsp;&nbsp;&nbsp;614⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63🍴</code></b> [aws-sdk-rails :fire::fire::fire:](https://github.com/aws/aws-sdk-rails))
* <b><code>&nbsp;&nbsp;&nbsp;235⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;88🍴</code></b> [appoxy/aws :fire::fire:](https://github.com/appoxy/aws))
* <b><code>&nbsp;&nbsp;&nbsp;450⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;173🍴</code></b> [rightscale/right_aws :fire::fire:](https://github.com/rightscale/right_aws))

### Rust SDK

* <b><code>&nbsp;&nbsp;2718⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;431🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/rusoto/rusoto))
* <b><code>&nbsp;&nbsp;2718⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;431🍴</code></b> [Install](https://github.com/rusoto/rusoto#installation))
* 🌎 [Docs](docs.rs/rusoto_core/)

*The Rust SDK is a community project with limited docs and/or samples.*

### Scala SDK

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;72⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;12🍴</code></b> [Repo](https://github.com/awslabs/aws-scala-sdk))

Related Repos:

* 🌎 [atlassian/aws-scala](bitbucket.org/atlassian/aws-scala)
* <b><code>&nbsp;&nbsp;&nbsp;727⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;219🍴</code></b> [seratch/AWScala :fire::fire::fire:](https://github.com/seratch/AWScala))

*The Scala SDK is a labs project with limited docs and/or samples.*

### Unity SDK

* <b><code>&nbsp;&nbsp;&nbsp;104⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;43🍴</code></b> [Repo :fire:](https://github.com/aws/aws-sdk-unity))
* <b><code>&nbsp;&nbsp;&nbsp;163⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;107🍴</code></b> [Repo with Samples :fire:](https://github.com/awslabs/aws-sdk-unity-samples))
* 🌎 [Install](s3.amazonaws.com/aws-unity-sdk/latest/aws-unity-sdk.zip)
* [Docs](http://docs.aws.amazon.com/mobile/sdkforunity/developerguide/)

### Xamarin SDK

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;45⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [Repo](https://github.com/awslabs/aws-sdk-xamarin))
* 🌎 [Blog with Samples](blog.xamarin.com/amazon-web-services-aws-mobile-sdks-for-xamarin-now-available/)

*The Xamarin SDK is a labs project with limited docs and/or samples.*

### .NET SDK

* <b><code>&nbsp;&nbsp;&nbsp;151⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;893🍴</code></b> [Repo :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-net))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;22⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [Repo with Samples](https://github.com/awslabs/aws-auto-scaling-console-sample))
* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* 🌎 [Docs](aws.amazon.com/documentation/sdk-for-net/)
* 🌎 [Learn More](aws.amazon.com/sdk-for-net/)
* <b><code>&nbsp;&nbsp;&nbsp;192⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;170🍴</code></b> [Samples :fire:](https://github.com/awslabs/aws-sdk-net-samples))

## Command Line Tools

*AWS and community command line tools with samples and docs.*

<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/commands.png">
</p>
<br/>

### Universal Command Line Interface

* <b><code>&nbsp;17318⭐</code></b> <b><code>&nbsp;&nbsp;4737🍴</code></b> [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cli))
* [Install](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)
* 🌎 [Docs](aws.amazon.com/documentation/cli/)
* 🌎 [Learn More](aws.amazon.com/cli/)

Related Repos:

* <b><code>&nbsp;&nbsp;7332⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;780🍴</code></b> [awslabs/aws-shell :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-shell))
* <b><code>&nbsp;&nbsp;5299⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;279🍴</code></b> [donnemartin/saws :fire::fire::fire::fire::fire:](https://github.com/donnemartin/saws))

### Windows PowerShell

* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* 🌎 [Docs](aws.amazon.com/documentation/powershell/)
* 🌎 [Learn More](aws.amazon.com/powershell/)

## IDE Toolkits

*Official IDE toolkits with samples and docs.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/x4nu914.png">
</p>
<br/>

### Eclipse Toolkit

* [Install](http://docs.aws.amazon.com/AWSToolkitEclipse/latest/ug/tke_setup.html)
* 🌎 [Docs](aws.amazon.com/documentation/awstoolkiteclipse/)
* 🌎 [Learn More](aws.amazon.com/eclipse/)

### Visual Studio Toolkit

* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* 🌎 [Docs](aws.amazon.com/documentation/aws-toolkit-visual-studio/)
* 🌎 [Learn More](aws.amazon.com/visualstudio/)

## Open Source Repos

*AWS and community open source projects, grouped by service.  See [A Note on Repo AWSomeness](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md#a-note-on-repo-awsomeness) for more details.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/wbhTgga.png">
</p>
<br/>

### API Gateway

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;307⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;109🍴</code></b> [api-gateway-secure-pet-store :fire::fire:](https://github.com/awslabs/api-gateway-secure-pet-store)) - Cognito credentials through Lambda.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;32⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [aws-apigateway-sdk-java](https://github.com/awslabs/aws-apigateway-sdk-java)) - SDK for Java.
* <b><code>&nbsp;&nbsp;&nbsp;518⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;137🍴</code></b> [aws-apigateway-swagger-importer :fire::fire::fire:](https://github.com/awslabs/aws-apigateway-importer)) - Tools to work with Swagger.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### CLI

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;485⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;80🍴</code></b> [awscli-aliases :fire::fire:](https://github.com/awslabs/awscli-aliases)) - Repository for AWS CLI aliases.
* <b><code>&nbsp;&nbsp;1804⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;296🍴</code></b> [amazon-ecs-cli :fire::fire::fire::fire:](https://github.com/aws/amazon-ecs-cli)) - ECS CLI using the same Docker Compose file format and familiar Compose commands.
* <b><code>&nbsp;17318⭐</code></b> <b><code>&nbsp;&nbsp;4737🍴</code></b> [aws-cli :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cli)) - Universal Command Line Interface.
* <b><code>&nbsp;&nbsp;7332⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;780🍴</code></b> [aws-shell :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-shell))
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;39⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;12🍴</code></b> [awscli-cookbook](https://github.com/awslabs/awscli-cookbook)) - Installs the CLI tools and provides a set of LWRPs for use within chef cookbooks.
* <b><code>&nbsp;&nbsp;&nbsp;142⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;27🍴</code></b> [awsmobile-cli :fire:](https://github.com/aws/awsmobile-cli)) - CLI experience for Frontend developers in the JavaScript ecosystem.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;842⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;39🍴</code></b> [achiku/jungle :fire::fire::fire:](https://github.com/achiku/jungle)) - Operations by EC2 and ELB cli should be simpler.
* <b><code>&nbsp;&nbsp;&nbsp;228⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;37🍴</code></b> [dbcli/athenacli :fire:](https://github.com/dbcli/athenacli)) - a CLI tool for AWS Athena service that can do auto-completion and syntax highlighting.
* <b><code>&nbsp;&nbsp;5299⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;279🍴</code></b> [donnemartin/saws :fire::fire::fire::fire::fire:](https://github.com/donnemartin/saws)) - A Supercharged AWS Command Line Interface.
* <b><code>&nbsp;&nbsp;&nbsp;440⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;130🍴</code></b> [timkay/aws :fire::fire:](https://github.com/timkay/aws)) - Easy command line access to Amazon EC2, S3, SQS, ELB, and SDB.
* <b><code>&nbsp;&nbsp;4960⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;257🍴</code></b> [wallix/awless :fire::fire::fire::fire::fire:](https://github.com/wallix/awless)) - a Powerful CLI for EC2, IAM and S3 in Go.
* <b><code>&nbsp;&nbsp;8999⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;825🍴</code></b> [99designs/aws-vault :fire::fire::fire::fire::fire:](https://github.com/99designs/aws-vault)) - A tool for securely storing AWS credentials, written in Go.

### CloudFormation

AWS Repos:

* <b><code>&nbsp;12948⭐</code></b> <b><code>&nbsp;&nbsp;4655🍴</code></b> [aws-cdk :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cdk)) - Framework for defining cloud infrastructure in code.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;86⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35🍴</code></b> [aws-cfn-custom-resource-examples](https://github.com/awslabs/aws-cfn-custom-resource-examples)) - Custom resource examples.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;71⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;37🍴</code></b> [aws-cfn-resource-bridge](https://github.com/aws/aws-cfn-resource-bridge)) - Custom resource framework.
* <b><code>&nbsp;&nbsp;2644⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;657🍴</code></b> [cfn-python-lint :fire::fire::fire::fire::fire:](https://github.com/awslabs/cfn-python-lint)) - A tool for linting/validating CloudFormation.
* <b><code>&nbsp;&nbsp;&nbsp;116⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;109🍴</code></b> [cfncluster-cookbook](https://github.com/awslabs/cfncluster-cookbook)) - Sample Cookbook.
* <b><code>&nbsp;&nbsp;&nbsp;887⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;314🍴</code></b> [cfncluster :fire::fire::fire:](https://github.com/awslabs/cfncluster)) - Framework that deploys and maintains HPC clusters.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;90⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [Appliscale/perun](https://github.com/Appliscale/perun)) - A CLI tool for linting/validation and managing CloudFormation templates and stacks.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [bazaarvoice/cloudformation-ruby-dsl :fire::fire:](https://github.com/bazaarvoice/cloudformation-ruby-dsl)) - Ruby DSL for creating templates.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;99⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33🍴</code></b> [beaknit/cform :fire:](https://github.com/beaknit/cform)) - SublimeText plugin.
* <b><code>&nbsp;&nbsp;1533⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;300🍴</code></b> [cloudreach/sceptre :fire::fire::fire::fire:](https://github.com/cloudreach/sceptre)) - A CLI tool for automating CloudFormation.
* <b><code>&nbsp;&nbsp;4941⭐</code></b> <b><code>&nbsp;&nbsp;1406🍴</code></b> [cloudtools/troposphere :fire::fire::fire::fire::fire:](https://github.com/cloudtools/troposphere)) - Python library to create descriptions.
* <b><code>&nbsp;&nbsp;&nbsp;204⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;36🍴</code></b> [peterkh/cumulus :fire::fire:](https://github.com/peterkh/cumulus)) - Manages stacks.
* <b><code>&nbsp;&nbsp;&nbsp;293⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;41🍴</code></b> [envato/stack_master :fire::fire:](https://github.com/envato/stack_master)) - A CLI tool to manage CloudFormation stacks.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;23🍴</code></b> [sparkleformation/sfn](https://github.com/sparkleformation/sfn)) - CLI for stack management.
* <b><code>&nbsp;&nbsp;&nbsp;221⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;44🍴</code></b> [sparkleformation/sparkle_formation :fire::fire:](https://github.com/sparkleformation/sparkle_formation)) - Ruby DSL for template creation.
* <b><code>&nbsp;&nbsp;1313⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;209🍴</code></b> [Stelligent/cfn_nag :fire::fire::fire::fire:](https://github.com/stelligent/cfn_nag)) - Linting tool for CloudFormation templates

### CloudSearch

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;22🍴</code></b> [cloudsearchable](https://github.com/awslabs/cloudsearchable)) - An ActiveRecord-style ORM query interface.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### CloudTrail

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;96⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;32🍴</code></b> [aws-cloudtrail-processing-library](https://github.com/aws/aws-cloudtrail-processing-library)) - Easily consume and process log files.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;358⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;50🍴</code></b> [AppliedTrust/traildash :fire::fire:](https://github.com/AppliedTrust/traildash)) - Slick dashboard.
* <b><code>&nbsp;&nbsp;&nbsp;459⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;162🍴</code></b> [GorillaStack/auto-tag :fire::fire:](https://github.com/GorillaStack/auto-tag)) - Automatically tag AWS resources on creation, for cost assignment.

### CloudWatch

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;398⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;142🍴</code></b> [cloudwatch-logs-subscription-consumer :fire::fire:](https://github.com/awslabs/cloudwatch-logs-subscription-consumer)) - Kinesis stream reader.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;70⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;67🍴</code></b> [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs)) - Assets in the blog post on using Amazon ECS and Amazon CloudWatch logs.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30🍴</code></b> [logstash-output-cloudwatchlogs](https://github.com/awslabs/logstash-output-cloudwatchlogs)) - A logstash plugin that sends logs to CloudWatch.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14🍴</code></b> [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks)) - OpsWorks sample cookbook.

Community Repos:

* <b><code>&nbsp;&nbsp;4993⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;343🍴</code></b> [jorgebastida/awslogs :fire::fire::fire::fire::fire:](https://github.com/jorgebastida/awslogs)) - Simple CLI for querying groups, streams and events.
* <b><code>&nbsp;&nbsp;&nbsp;152⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;82🍴</code></b> [newrelic-platform/newrelic_aws_cloudwatch_plugin :fire:](https://github.com/newrelic-platform/newrelic_aws_cloudwatch_plugin)) - New Relic plugin.

### Code Deploy

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;337⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;195🍴</code></b> [aws-codedeploy-agent :fire::fire:](https://github.com/aws/aws-codedeploy-agent)) - Sample agent.
* <b><code>&nbsp;&nbsp;&nbsp;156⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;130🍴</code></b> [aws-codedeploy-plugin :fire:](https://github.com/awslabs/aws-codedeploy-plugin)) - Jenkins plugin.
* <b><code>&nbsp;&nbsp;&nbsp;639⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;775🍴</code></b> [aws-codedeploy-samples :fire::fire::fire:](https://github.com/awslabs/aws-codedeploy-samples)) - Samples and template scenarios.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Code Pipeline

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;31⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;21🍴</code></b> [aws-codepipeline-custom-job-worker](https://github.com/awslabs/aws-codepipeline-custom-job-worker)) - Develop your own job worker when creating a custom action.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51⭐</code></b> <b><code>&nbsp;&nbsp;1435🍴</code></b> [aws-codepipeline-jenkins-aws-codedeploy_linux](https://github.com/awslabs/aws-codepipeline-jenkins-aws-codedeploy_linux)) - Four-stage pipeline for Linux.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;82⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;71🍴</code></b> [aws-codepipeline-plugin-for-jenkins](https://github.com/awslabs/aws-codepipeline-plugin-for-jenkins)) - Jenkins plugin.
* <b><code>&nbsp;&nbsp;&nbsp;173⭐</code></b> <b><code>&nbsp;&nbsp;6077🍴</code></b> [aws-codepipeline-s3-aws-codedeploy_linux :fire:](https://github.com/awslabs/aws-codepipeline-s3-aws-codedeploy_linux)) - Simple pipeline for Linux.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;281🍴</code></b> [AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows)) - Four-stage pipeline for Windows.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;47🍴</code></b> [AWSCodePipeline-S3-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-S3-AWSCodeDeploy_Windows)) - Simple pipeline for Windows.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Cognito

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;31⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;15🍴</code></b> [amazon-cognito-android](https://github.com/aws/amazon-cognito-android)) - Sync SDK for Android.
* <b><code>&nbsp;&nbsp;&nbsp;100⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;47🍴</code></b> [amazon-cognito-developer-authentication-sample](https://github.com/awslabs/amazon-cognito-developer-authentication-sample)) - Authentication sample.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7🍴</code></b> [amazon-cognito-dotnet](https://github.com/aws/amazon-cognito-dotnet)) - Sync SDK for .NET.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [amazon-cognito-ios](https://github.com/aws/amazon-cognito-ios)) - Sync SDK for iOS.
* <b><code>&nbsp;&nbsp;&nbsp;199⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;71🍴</code></b> [amazon-cognito-js :fire::fire:](https://github.com/aws/amazon-cognito-js)) - Sync SDK for JavaScript.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [amazon-cognito-streams-sample](https://github.com/awslabs/amazon-cognito-streams-sample)) - Consuming Streams sample.
* <b><code>&nbsp;&nbsp;&nbsp;121⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;37🍴</code></b> [cognito-sample-nodejs :fire:](https://github.com/awslabs/cognito-sample-nodejs)) - Sample App for Node.js.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;473⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;186🍴</code></b> [capeless/warrant :fire::fire:](https://github.com/capless/warrant)) - Python library for using Cognito.
* <b><code>&nbsp;&nbsp;&nbsp;201⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;64🍴</code></b> [rahulpsd18/cognito-backup-restore :fire:](https://github.com/rahulpsd18/cognito-backup-restore)) - Tool for backing up and restoring Cognito user pools.

### Data Pipeline

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;470⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;258🍴</code></b> [data-pipeline-samples :fire::fire:](https://github.com/awslabs/data-pipeline-samples)) - Sample pipelines.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Device Farm

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;92⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;77🍴</code></b> [aws-device-farm-appium-tests-for-sample-app](https://github.com/awslabs/aws-device-farm-appium-tests-for-sample-app)) - Appium TestNG Android tests.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;13🍴</code></b> [aws-device-farm-calabash-tests-for-sample-app](https://github.com/awslabs/aws-device-farm-calabash-tests-for-sample-app)) - Calabash Android tests.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;60⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;27🍴</code></b> [aws-device-farm-gradle-plugin](https://github.com/awslabs/aws-device-farm-gradle-plugin)) - Gradle plugin.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;88⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;67🍴</code></b> [aws-device-farm-jenkins-plugin](https://github.com/awslabs/aws-device-farm-jenkins-plugin)) - Jenkins plugin.
* <b><code>&nbsp;&nbsp;&nbsp;174⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;205🍴</code></b> [aws-device-farm-sample-app-for-android :fire:](https://github.com/awslabs/aws-device-farm-sample-app-for-android)) - Sample Android app.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### DynamoDB

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;43⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [aws-dotnet-session-provider](https://github.com/aws/aws-dotnet-session-provider)) - A session state provider for ASP.NET apps.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;15⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;12🍴</code></b> [aws-dotnet-trace-listener](https://github.com/aws/aws-dotnet-trace-listener)) - A trace listener for System.Diagnostics that can be used to log events.
* <b><code>&nbsp;&nbsp;&nbsp;141⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;74🍴</code></b> [aws-dynamodb-encryption-java :fire:](https://github.com/awslabs/aws-dynamodb-encryption-java)) - Encryption Client for Java.
* <b><code>&nbsp;&nbsp;&nbsp;605⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;242🍴</code></b> [aws-dynamodb-examples :fire::fire:](https://github.com/awslabs/aws-dynamodb-examples)) - Samples using the Java SDK.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [aws-dynamodb-mars-json-demo](https://github.com/awslabs/aws-dynamodb-mars-json-demo)) - Stores and indexes NASA JPL Mars images.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;98⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;72🍴</code></b> [aws-dynamodb-session-tomcat](https://github.com/aws/aws-dynamodb-session-tomcat)) - Session store for Apache Tomcat.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;69⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;28🍴</code></b> [aws-sessionstore-dynamodb-ruby](https://github.com/aws/aws-sessionstore-dynamodb-ruby)) - Handles sessions for Ruby web apps.
* <b><code>&nbsp;&nbsp;&nbsp;275⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;87🍴</code></b> [dynamodb-cross-region-library :fire::fire:](https://github.com/awslabs/dynamodb-cross-region-library)) - Cross-region replication.
* <b><code>&nbsp;&nbsp;&nbsp;275⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;93🍴</code></b> [dynamodb-geo :fire::fire:](https://github.com/awslabs/dynamodb-geo)) - Library to create and query geospatial data.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;88⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;36🍴</code></b> [dynamodb-import-export-tool](https://github.com/awslabs/dynamodb-import-export-tool)) - Import and export examples.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9🍴</code></b> [dynamodb-online-index-violation-detector](https://github.com/awslabs/dynamodb-online-index-violation-detector)) - Finds violations on an online GSI's hash key and range key.
* <b><code>&nbsp;&nbsp;&nbsp;103⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;44🍴</code></b> [dynamodb-streams-kinesis-adapter](https://github.com/awslabs/dynamodb-streams-kinesis-adapter)) - Kinesis interface to consume and process data from a DynamoDB stream.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;49⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [dynamodb-tictactoe-example-app](https://github.com/awslabs/dynamodb-tictactoe-example-app)) - Lightweight python app.
* <b><code>&nbsp;&nbsp;&nbsp;446⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;94🍴</code></b> [dynamodb-titan-storage-backend :fire::fire:](https://github.com/awslabs/dynamodb-titan-storage-backend)) - Storage Backend for Titan.
* <b><code>&nbsp;&nbsp;&nbsp;358⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;86🍴</code></b> [dynamodb-transactions :fire::fire:](https://github.com/awslabs/dynamodb-transactions)) - Performs atomic writes and isolated reads across multiple items and tables.
* <b><code>&nbsp;&nbsp;&nbsp;104⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [logstash-input-dynamodb :fire:](https://github.com/awslabs/logstash-input-dynamodb)) - Logstash input plugin.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;309⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;82🍴</code></b> [channl/dynamodb-lambda-autoscale :fire::fire:](https://github.com/channl/dynamodb-lambda-autoscale)) - Autoscale DynamoDB provisioned capacity using Lambda.
* <b><code>&nbsp;&nbsp;1853⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;106🍴</code></b> [lyft/confidant :fire::fire::fire::fire:](https://github.com/lyft/confidant)) - Stores secrets, encrypted at rest.
* <b><code>&nbsp;&nbsp;&nbsp;618⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [sebdah/dynamic-dynamodb :fire::fire::fire:](https://github.com/sebdah/dynamic-dynamodb)) - Provides auto-scaling.
* <b><code>&nbsp;&nbsp;&nbsp;716⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;108🍴</code></b> [sensedeep/dynamodb-onetable :fire::fire::fire:](https://github.com/sensedeep/dynamodb-onetable)) - DynamoDB library for single table designs using NodeJS.

### Elastic Beanstalk

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;29🍴</code></b> [aws-eb-glassfish-dockerfiles](https://github.com/aws/aws-eb-glassfish-dockerfiles)) - GlassFish docker files.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;61⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33🍴</code></b> [aws-eb-python-dockerfiles](https://github.com/aws/aws-eb-python-dockerfiles)) - Python docker files.
* <b><code>&nbsp;&nbsp;&nbsp;145⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;177🍴</code></b> [eb-demo-php-simple-app :fire:](https://github.com/awslabs/eb-demo-php-simple-app)) - Simple PHP app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;58⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;31🍴</code></b> [eb-docker-multiple-ports](https://github.com/awslabs/eb-docker-multiple-ports)) - Simple Node.js and Tomcat apps using Docker images.
* <b><code>&nbsp;&nbsp;&nbsp;145⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;83🍴</code></b> [eb-docker-nginx-proxy :fire:](https://github.com/awslabs/eb-docker-nginx-proxy)) - Simple PHP app using the PHP-FPM and Nginx Docker images.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9🍴</code></b> [eb-docker-virtual-hosting](https://github.com/awslabs/eb-docker-virtual-hosting)) - Simple PHP, Tomcat, and Nginx applications using Docker images.
* <b><code>&nbsp;&nbsp;&nbsp;279⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;247🍴</code></b> [eb-node-express-sample :fire::fire:](https://github.com/awslabs/eb-node-express-sample)) - Sample express app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;77⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;97🍴</code></b> [eb-node-express-signup](https://github.com/awslabs/eb-node-express-signup)) - Express framework and Bootstrap Node.js sample app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10🍴</code></b> [eb-node-express](https://github.com/awslabs/eb-node-express)) - Sample app referenced in the Developer Guide.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;43⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;22🍴</code></b> [eb-py-flask-signup-worker](https://github.com/awslabs/eb-py-flask-signup-worker)) - Python app that illustrates worker roles.
* <b><code>&nbsp;&nbsp;&nbsp;265⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;157🍴</code></b> [eb-py-flask-signup :fire::fire:](https://github.com/awslabs/eb-py-flask-signup)) - Python signup form app with Flask and Bootstrap.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;37⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;69🍴</code></b> [eb-python-flask](https://github.com/awslabs/eb-python-flask)) - Simple Python and Flask app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;17⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9🍴</code></b> [eb-wif-sample](https://github.com/awslabs/eb-wif-sample)) - Sample login app with Web Identity Federation.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;189⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;24🍴</code></b> [alienfast/elastic-beanstalk :fire:](https://github.com/alienfast/elastic-beanstalk)) - Gem with rake configuration and deployment for rails apps.
* <b><code>&nbsp;&nbsp;&nbsp;389⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;89🍴</code></b> [ThoughtWorksStudios/eb_deployer :fire::fire:](https://github.com/ThoughtWorksStudios/eb_deployer)) - Blue-green deployment automation.

### Elastic Compute Cloud

AWS Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;435⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;103🍴</code></b> [alestic/ec2-consistent-snapshot :fire::fire:](https://github.com/alestic/ec2-consistent-snapshot)) - Initiate consistent EBS snapshots in EC2.
* <b><code>&nbsp;&nbsp;&nbsp;558⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30🍴</code></b> [ConradIrwin/aws-name-server :fire::fire::fire:](https://github.com/ConradIrwin/aws-name-server)) - DNS server that lets you look up instances by name.
* <b><code>&nbsp;&nbsp;2372⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;311🍴</code></b> [cristim/autospotting :fire::fire::fire::fire::fire:](https://github.com/autospotting/autospotting)) - Automatically rolling-replace on-demand EC2 instances in AutoScaling groups with compatible spot instances.
* <b><code>&nbsp;&nbsp;&nbsp;208⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;120🍴</code></b> [evannuil/aws-snapshot-tool :fire::fire:](https://github.com/evannuil/aws-snapshot-tool)) - Automates EBS snapshots and rotation.
* <b><code>&nbsp;50448⭐</code></b> <b><code>&nbsp;15926🍴</code></b> [kelseyhightower/kubernetes-the-hard-way :fire::fire::fire::fire::fire:](https://github.com/kelseyhightower/kubernetes-the-hard-way)) - Bootstrap Kubernetes the hard way on EC2. No scripts.
* <b><code>&nbsp;&nbsp;&nbsp;252⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;37🍴</code></b> [mirakui/ec2ssh :fire::fire:](https://github.com/mirakui/ec2ssh)) - SSH config manager.
* <b><code>&nbsp;&nbsp;9834⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;983🍴</code></b> [openebs/openebs :fire::fire::fire::fire::fire:](https://github.com/openebs/openebs)) - Containerized block storage QoS SLAs, tiering and replica policies across AZs and environments, and predictable and scalable performance.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [skavanagh/EC2Box :fire::fire:](https://github.com/skavanagh/EC2Box)) - A web-based SSH console to manage multiple instances simultaneously.
* <b><code>&nbsp;&nbsp;&nbsp;164⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7🍴</code></b> [wbailey/claws :fire:](https://github.com/wbailey/claws)) - CLI-driven console with capistrano integration.

### Elastic Container Service

AWS Repos:

* <b><code>&nbsp;&nbsp;2185⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;665🍴</code></b> [amazon-ecs-agent :fire::fire::fire::fire:](https://github.com/aws/amazon-ecs-agent)) - Agent that runs on and starts containers.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;66⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [amazon-ecs-amazon-efs](https://github.com/awslabs/amazon-ecs-amazon-efs)) - Persists Data from containers.
* <b><code>&nbsp;&nbsp;&nbsp;197⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;109🍴</code></b> [amazon-ecs-init :fire:](https://github.com/aws/amazon-ecs-init)) - RPM developed to support the Amazon ECS Container Agent.
* <b><code>&nbsp;&nbsp;&nbsp;938⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;73🍴</code></b> [blox :fire::fire::fire:](https://github.com/blox/blox)) - Open source tools for building custom schedulers on ECS.
* <b><code>&nbsp;&nbsp;&nbsp;460⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;451🍴</code></b> [ecs-blue-green-deployment :fire::fire:](https://github.com/awslabs/ecs-blue-green-deployment)) - Blue-green deployment on ECS.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;70⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;67🍴</code></b> [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs)) - Assets from the blog using Amazon ECS and Amazon CloudWatch logs.
* <b><code>&nbsp;&nbsp;&nbsp;173⭐</code></b> <b><code>&nbsp;&nbsp;3236🍴</code></b> [ecs-demo-php-simple-app :fire:](https://github.com/awslabs/ecs-demo-php-simple-app)) - Simple PHP app.
* <b><code>&nbsp;&nbsp;&nbsp;173⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;13🍴</code></b> [ecs-mesos-scheduler-driver :fire:](https://github.com/awslabs/ecs-mesos-scheduler-driver)) - Integrates Apache Mesos.
* <b><code>&nbsp;&nbsp;&nbsp;852⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;961🍴</code></b> [ecs-refarch-continuous-deployment :fire::fire::fire:](https://github.com/awslabs/ecs-refarch-continuous-deployment)) - Reference Architecture for continuous deployment to ECS using CodePipeline.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;61⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;13🍴</code></b> [ecs-task-kite](https://github.com/awslabs/ecs-task-kite)) - Simple ambassador container for inter-task communication.
* <b><code>&nbsp;&nbsp;&nbsp;294⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;46🍴</code></b> [lambda-ecs-worker-pattern :fire::fire:](https://github.com/awslabs/lambda-ecs-worker-pattern)) - Extends Lambda using SQS and ECS.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;79⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;499🍴</code></b> [py-flask-signup-docker](https://github.com/awslabs/py-flask-signup-docker)) - Python sample app.
* <b><code>&nbsp;&nbsp;&nbsp;107⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;52🍴</code></b> [service-discovery-ecs-consul :fire:](https://github.com/awslabs/service-discovery-ecs-consul)) - Assets from the blog Service Discovery via Consul with Amazon ECS.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;44⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [Lumoslabs/broadside](https://github.com/lumoslabs/broadside)) - Command line tool for deploying revisions of containerized applications.
* <b><code>&nbsp;&nbsp;&nbsp;965⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;133🍴</code></b> [Stelligent/mu :fire::fire::fire:](https://github.com/stelligent/mu)) - Command line tool to simplify ECS deployments via CodeBuild and CodePipeline.

### Elastic File System

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;66⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [amazon-ecs-amazon-efs](https://github.com/awslabs/amazon-ecs-amazon-efs)) - Persist data from ECS.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Elastic MapReduce

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;613⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;301🍴</code></b> [emr-bootstrap-actions :fire::fire::fire:](https://github.com/awslabs/emr-bootstrap-actions)) - Sample bootstrap actions.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51🍴</code></b> [emr-sample-apps](https://github.com/awslabs/emr-sample-apps)) - Sample apps.

Community Repos:

* <b><code>&nbsp;&nbsp;2614⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;577🍴</code></b> [Yelp/mrjob :fire::fire::fire::fire::fire:](https://github.com/Yelp/mrjob)) - Run MapReduce jobs on Hadoop or EMR.

### Elastic Search

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;374⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;100🍴</code></b> [logstash-output-amazon_es :fire::fire:](https://github.com/awslabs/logstash-output-amazon_es)) - Logstash output plugin to sign and export events.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;116🍴</code></b> [opsworks-elasticsearch-cookbook](https://github.com/awslabs/opsworks-elasticsearch-cookbook)) - OpsWorks Elasticsearch sample cookbook.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;576⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;179🍴</code></b> [elastic/elasticsearch-cloud-aws :fire::fire::fire:](https://github.com/elastic/elasticsearch-cloud-aws)) - Plugin for Elasticsearch.

### Elasticache

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;24🍴</code></b> [aws-elasticache-cluster-client-libmemcached](https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached)) - Libmemcached library support.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;93⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;57🍴</code></b> [aws-elasticache-cluster-client-memcached-for-java](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-java)) - Client for Java.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;65⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [aws-elasticache-cluster-client-memcached-for-php](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php)) - Enhanced PHP library connecting to ElastiCache.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;29⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;16🍴</code></b> [elasticache-cluster-config-net](https://github.com/awslabs/elasticache-cluster-config-net)) - Config object for Enyim's MemcachedClient to enable auto discovery.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Glacier

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;537⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;53🍴</code></b> [vsespb/mt-aws-glacier :fire::fire::fire:](https://github.com/vsespb/mt-aws-glacier)) - Perl Multithreaded Multipart sync to Glacier.

### Kinesis

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;151⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30🍴</code></b> [amazon-kinesis-aggregators :fire:](https://github.com/awslabs/amazon-kinesis-aggregators)) - Provides a simple way to create real time aggregations.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;62⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;68🍴</code></b> [amazon-kinesis-client-net](https://github.com/awslabs/amazon-kinesis-client-net)) - Client Library for .NET.
* <b><code>&nbsp;&nbsp;&nbsp;303⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;199🍴</code></b> [amazon-kinesis-client-nodejs :fire::fire:](https://github.com/awslabs/amazon-kinesis-client-nodejs)) - Client Library for Node.js.
* <b><code>&nbsp;&nbsp;&nbsp;377⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;229🍴</code></b> [amazon-kinesis-client-python :fire::fire:](https://github.com/awslabs/amazon-kinesis-client-python)) - Client Library for Python.
* <b><code>&nbsp;&nbsp;&nbsp;147⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;61🍴</code></b> [amazon-kinesis-client-ruby :fire:](https://github.com/awslabs/amazon-kinesis-client-ruby)) - Client Library for Ruby.
* <b><code>&nbsp;&nbsp;&nbsp;668⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;487🍴</code></b> [amazon-kinesis-client :fire::fire::fire:](https://github.com/awslabs/amazon-kinesis-client)) Client library for Amazon Kinesis.
* <b><code>&nbsp;&nbsp;&nbsp;327⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;184🍴</code></b> [amazon-kinesis-connectors :fire::fire:](https://github.com/awslabs/amazon-kinesis-connectors)) - Libary to integrate with other AWS and non-AWS services.
* <b><code>&nbsp;&nbsp;&nbsp;171⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;94🍴</code></b> [amazon-kinesis-data-visualization-sample :fire:](https://github.com/awslabs/amazon-kinesis-data-visualization-sample)) - Sample data visualization app.
* <b><code>&nbsp;&nbsp;&nbsp;112⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;137🍴</code></b> [amazon-kinesis-learning](https://github.com/awslabs/amazon-kinesis-learning)) - Learning Kinesis Development.
* <b><code>&nbsp;&nbsp;&nbsp;415⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;342🍴</code></b> [amazon-kinesis-producer :fire::fire:](https://github.com/awslabs/amazon-kinesis-producer)) - Producer Library.
* <b><code>&nbsp;&nbsp;&nbsp;335⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;84🍴</code></b> [amazon-kinesis-scaling-utils :fire::fire:](https://github.com/awslabs/amazon-kinesis-scaling-utils)) - Provides the ability to scale streams.
* <b><code>&nbsp;&nbsp;&nbsp;289⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;96🍴</code></b> [aws-fluent-plugin-kinesis :fire::fire:](https://github.com/awslabs/aws-fluent-plugin-kinesis)) - Fluent Plugin.
* <b><code>&nbsp;&nbsp;&nbsp;103⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;44🍴</code></b> [dynamodb-streams-kinesis-adapter](https://github.com/awslabs/dynamodb-streams-kinesis-adapter)) - DynamoDB Streams Adapter.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;41🍴</code></b> [kinesis-log4j-appender](https://github.com/awslabs/kinesis-log4j-appender)) - Log4J Appender.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;69⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;20🍴</code></b> [kinesis-poster-worker](https://github.com/awslabs/kinesis-poster-worker)) - Simple multi-threaded Python Poster and Worker.
* <b><code>&nbsp;&nbsp;&nbsp;108⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;61🍴</code></b> [kinesis-storm-spout :fire:](https://github.com/awslabs/kinesis-storm-spout)) - Spout for Storm.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;40⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14🍴</code></b> [mqtt-kinesis-bridge](https://github.com/awslabs/mqtt-kinesis-bridge)) - Simple MQTT bridge in Python.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Lambda

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;386⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;170🍴</code></b> [amazon-elasticsearch-lambda-samples :fire::fire:](https://github.com/awslabs/amazon-elasticsearch-lambda-samples)) - Data ingestion for Elasticsearch from S3 and Kinesis.
* <b><code>&nbsp;&nbsp;6738⭐</code></b> <b><code>&nbsp;&nbsp;1256🍴</code></b> [awslabs/aws-sam-local :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-sam-local)) - CLI tool for local development and testing of Serverless applications.
* <b><code>&nbsp;&nbsp;3801⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;581🍴</code></b> [aws-lambda-go :fire::fire::fire::fire::fire:](https://github.com/aws/aws-lambda-go)) - Libraries, samples and tools to help Go developers develop Lambda functions.
* <b><code>&nbsp;&nbsp;&nbsp;549⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;241🍴</code></b> [aws-lambda-java-libs :fire::fire:](https://github.com/aws/aws-lambda-java-libs)) - Official mirror for interface definitions and helper classes.
* <b><code>&nbsp;&nbsp;&nbsp;595⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;161🍴</code></b> [aws-lambda-redshift-loader :fire::fire::fire:](https://github.com/awslabs/aws-lambda-redshift-loader)) - Redshift loader.
* <b><code>&nbsp;11057⭐</code></b> <b><code>&nbsp;&nbsp;1017🍴</code></b> [chalice :fire::fire::fire::fire::fire:](https://github.com/awslabs/chalice)) - Python Serverless Microframework.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;28⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [create-thumbnails-lambda](https://github.com/awslabs/create-thumbnails-lambda)) - Uses the grunt-aws-lambda plugin to help you develop and test.
* <b><code>&nbsp;&nbsp;&nbsp;294⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;46🍴</code></b> [lambda-ecs-worker-pattern :fire::fire:](https://github.com/awslabs/lambda-ecs-worker-pattern)) - Extends Lambda using SQS and ECS.
* <b><code>&nbsp;&nbsp;&nbsp;471⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;175🍴</code></b> [lambda-refarch-fileprocessing :fire::fire:](https://github.com/awslabs/lambda-refarch-fileprocessing)) - Reference Architecture for Real-time File Processing.
* <b><code>&nbsp;&nbsp;&nbsp;250⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;83🍴</code></b> [lambda-refarch-iotbackend :fire::fire:](https://github.com/awslabs/lambda-refarch-iotbackend)) - Reference Architecture for creating an IoT Backend.
* <b><code>&nbsp;&nbsp;&nbsp;587⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;108🍴</code></b> [lambda-refarch-mobilebackend :fire::fire::fire:](https://github.com/awslabs/lambda-refarch-mobilebackend)) - Reference Architecture for creating a Mobile Backend.
* <b><code>&nbsp;&nbsp;1586⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;899🍴</code></b> [lambda-refarch-webapp :fire::fire::fire::fire:](https://github.com/awslabs/lambda-refarch-webapp)) - Reference Architecture for creating a Web Application.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;530⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;36🍴</code></b> [alestic/lambdash :fire::fire::fire:](https://github.com/alestic/lambdash)) - Lambda shell - Run sh commands inside the Lambda environment.
* <b><code>&nbsp;&nbsp;&nbsp;227⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10🍴</code></b> [Alephbet/gimel :fire::fire:](https://github.com/Alephbet/gimel)) - Run your own A/B testing backend using Lambda.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;56🍴</code></b> [apex/apex ](https://github.com/apex/apex)) - Minimal AWS Lambda function manager with Go support.
* <b><code>&nbsp;&nbsp;3884⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;276🍴</code></b> [claudiajs/claudia :fire::fire::fire::fire::fire:](https://github.com/claudiajs/claudia)) - Deploy Node.js projects to Lambda and API Gateway easily.
* <b><code>&nbsp;&nbsp;&nbsp;388⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63🍴</code></b> [cloudnative/lambda-chat :fire::fire:](https://github.com/cloudnative/lambda-chat)) - A chat application without servers.
* <b><code>&nbsp;&nbsp;1364⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;223🍴</code></b> [danilop/LambdAuth :fire::fire::fire::fire:](https://github.com/danilop/LambdAuth)) - Sample authentication service.
* <b><code>&nbsp;&nbsp;&nbsp;696⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33🍴</code></b> [eawsy/aws-lambda-go :fire::fire::fire:](https://github.com/eawsy/aws-lambda-go)) - A fast and clean way to execute Go on Lambda.
* <b><code>&nbsp;&nbsp;&nbsp;894⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;83🍴</code></b> [garnaat/kappa :fire::fire::fire:](https://github.com/garnaat/kappa)) - Kappa is a CLI tool that makes it easier to deploy, update, and test functions for AWS Lambda.
* <b><code>&nbsp;&nbsp;1863⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;182🍴</code></b> [goadapp/goad :fire::fire::fire::fire:](https://github.com/goadapp/goad)) - Lambda powered, highly distributed, load testing tool.
* <b><code>&nbsp;13215⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;568🍴</code></b> [graphcool/chromeless :fire::fire::fire::fire::fire:](https://github.com/graphcool/chromeless)) - Automate Chrome through Lambda.
* <b><code>&nbsp;&nbsp;&nbsp;598⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;47🍴</code></b> [grycap/scar :fire::fire::fire:](https://github.com/grycap/scar)) - Transparently execute containers out of Docker images in AWS Lambda.
* <b><code>&nbsp;&nbsp;1471⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;127🍴</code></b> [jeremydaly/lambda-api :fire::fire::fire::fire:](https://github.com/jeremydaly/lambda-api)) - Lightweight web framework for your serverless applications.
* <b><code>&nbsp;&nbsp;&nbsp;620⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;28🍴</code></b> [jimpick/lambda-comments :fire::fire::fire:](https://github.com/jimpick/lambda-comments)) - Blog commenting system built with Lambda.
* <b><code>&nbsp;&nbsp;2027⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;131🍴</code></b> [jorgebastida/gordon :fire::fire::fire::fire::fire:](https://github.com/jorgebastida/gordon)) - λ Gordon is a tool to create, wire and deploy AWS Lambdas using CloudFormation.
* <b><code>&nbsp;&nbsp;1286⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [ks888/LambStatus :fire::fire::fire::fire:](https://github.com/ks888/LambStatus)) - A status page system inspired by StatusPage.io, built on AWS Lambda.
* <b><code>&nbsp;&nbsp;&nbsp;565⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;12🍴</code></b> [kubek2k/lambdoku :fire::fire::fire:](https://github.com/kubek2k/lambdoku)) - Heroku-like experience when using Lambda.
* <b><code>&nbsp;&nbsp;3962⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;183🍴</code></b> [lambci/lambci :fire::fire::fire::fire::fire:](https://github.com/lambci/lambci)) - A continuous integration system built on Lambda.
* <b><code>&nbsp;&nbsp;1058⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;47🍴</code></b> [littlstar/s3-lambda :fire::fire::fire::fire:](https://github.com/littlstar/s3-lambda)) - Lambda functions over S3 objects with concurrency control (each, map, reduce, filter).
* <b><code>&nbsp;&nbsp;1262⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35🍴</code></b> [mentum/lambdaws :fire::fire::fire::fire:](https://github.com/mentum/lambdaws)) - Deploy, run and get results in a breeze.
* <b><code>&nbsp;11814⭐</code></b> <b><code>&nbsp;&nbsp;1167🍴</code></b> [Miserlou/Zappa :fire::fire::fire::fire::fire:](https://github.com/Miserlou/Zappa)) - Serverless WSGI Python Web Apps with AWS Lambda + API Gateway.
* <b><code>&nbsp;&nbsp;1512⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;227🍴</code></b> [nficano/python-lambda :fire::fire::fire::fire:](https://github.com/nficano/python-lambda)) - A toolkit for developing and deploying serverless Python code in Lambda.
* <b><code>&nbsp;46933⭐</code></b> <b><code>&nbsp;&nbsp;5716🍴</code></b> [serverless/serverless :fire::fire::fire::fire::fire:](https://github.com/serverless/serverless)) The Serverless Application Framework (formerly JAWS).
* <b><code>&nbsp;&nbsp;&nbsp;243⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;98🍴</code></b> [Tim-B/grunt-aws-lambda :fire::fire:](https://github.com/Tim-B/grunt-aws-lambda)) - Grunt plugin.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [trek10inc/aws-lambda-debugger :fire::fire:](https://github.com/trek10inc/aws-lambda-debugger)) - Remote debugging tool for Lambda functions running on Node 6.10

### Machine Learning

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;879⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;387🍴</code></b> [machine-learning-samples :fire::fire::fire:](https://github.com/awslabs/machine-learning-samples)) - Sample apps.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Mobile Analytics

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;83⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;24🍴</code></b> [aws-sdk-mobile-analytics-js](https://github.com/aws/aws-sdk-mobile-analytics-js)) - JavaScript SDK.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### OpsWorks

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5🍴</code></b> [opsworks-attribute-customization](https://github.com/awslabs/opsworks-attribute-customization)) - Attribute customization example.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5🍴</code></b> [opsworks-capistrano](https://github.com/awslabs/opsworks-capistrano)) - Capistrano with instances.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14🍴</code></b> [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks)) - CloudWatch sample cookbook.
* <b><code>&nbsp;&nbsp;1042⭐</code></b> <b><code>&nbsp;&nbsp;1183🍴</code></b> [opsworks-cookbooks :fire::fire::fire::fire:](https://github.com/aws/opsworks-cookbooks)) - Chef Cookbooks.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;16⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;22🍴</code></b> [opsworks-demo-php-photo-share-app](https://github.com/awslabs/opsworks-demo-php-photo-share-app)) - Simple PHP photo share app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;44⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;192🍴</code></b> [opsworks-demo-php-simple-app](https://github.com/awslabs/opsworks-demo-php-simple-app)) - Simple PHP app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;39🍴</code></b> [opsworks-demo-rails-photo-share-app](https://github.com/awslabs/opsworks-demo-rails-photo-share-app)) - A sample Rails app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;116🍴</code></b> [opsworks-elasticsearch-cookbook](https://github.com/awslabs/opsworks-elasticsearch-cookbook)) - Elasticsearch sample cookbook.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;96⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;139🍴</code></b> [opsworks-example-cookbooks :fire:](https://github.com/awslabs/opsworks-example-cookbooks)) - Cookbooks used with the sample apps.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;39🍴</code></b> [opsworks-first-cookbook](https://github.com/awslabs/opsworks-first-cookbook)) - Cookbook used to demonstrate simple recipes.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;393🍴</code></b> [opsworks-windows-demo-](https://github.com/awslabs/opsworks-windows-demo-nodejs)) - A sample Node.JS app.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;16🍴</code></b> [opsworks-windows-demo-cookbooks](https://github.com/awslabs/opsworks-windows-demo-cookbooks)) - Cookbooks for Windows.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7🍴</code></b> [todo-sample-app-cookbooks](https://github.com/awslabs/todo-sample-app-cookbooks)) - Custom cookbooks associated with the todo-sample-app.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### Redshift

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;595⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;161🍴</code></b> [aws-lambda-redshift-loader :fire::fire::fire:](https://github.com/awslabs/aws-lambda-redshift-loader)) - Lambda database loader.
* <b><code>&nbsp;&nbsp;2802⭐</code></b> <b><code>&nbsp;&nbsp;1240🍴</code></b> [amazon-redshift-utils :fire::fire::fire::fire::fire:](https://github.com/awslabs/amazon-redshift-utils)) - Applies optimal Column Encoding to existing Tables.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;76⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;12🍴</code></b> [Lumoslabs/aleph](https://github.com/lumoslabs/aleph)) - A full featured web application for writing and running Redshift
queries. Supports revision tracking of queries and has basic visualization support.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [getredash/redash :fire::fire::fire::fire::fire:](https://github.com/getredash/redash/)) - A web application that allows to easily query an existing database, share the dataset and visualize it in different ways. Initially was developed to work with Redshift, and has great support for it.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;92⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;22🍴</code></b> [everythingMe/redshift_console](https://github.com/EverythingMe/redshift_console)) -  A simple tool to monitor and manage a Redshift cluster. The first release has basic tools to monitor running queries, WLM queue and your tables/schemas.

### Route 53

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;362⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [route53-infima :fire::fire:](https://github.com/awslabs/route53-infima)) - Manages service-level fault isolation.

Community Repos:

* <b><code>&nbsp;&nbsp;2137⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;265🍴</code></b> [barnybug/cli53 :fire::fire::fire::fire:](https://github.com/barnybug/cli53)) - cli53 is a command line tool for Amazon Route 53 which provides import and export from BIND format and simple command line management of Route 53 domains.
* <b><code>&nbsp;&nbsp;&nbsp;324⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;43🍴</code></b> [winebarrel/roadworker :fire::fire:](https://github.com/winebarrel/roadworker)) - Roadworker is a tool to manage Route53. It defines the state of Route53 using DSL, and updates Route53 according to DSL.

### S3

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;476⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;140🍴</code></b> [anomalizer/ngx_aws_auth :fire::fire:](https://github.com/anomalizer/ngx_aws_auth)) - Implements proxying of authenticated requests.
* <b><code>&nbsp;&nbsp;1396⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;208🍴</code></b> [bloomreach/s4cmd :fire::fire::fire::fire:](https://github.com/bloomreach/s4cmd)) - S3 command line tool, faster than S3cmd for large files.
* <b><code>&nbsp;&nbsp;&nbsp;589⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;102🍴</code></b> [CulturalMe/meteor-slingshot :fire::fire::fire:](https://github.com/CulturalMe/meteor-slingshot)) - Upload files in meteor.
* <b><code>&nbsp;&nbsp;&nbsp;660⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;92🍴</code></b> [danilop/yas3fs :fire::fire::fire:](https://github.com/danilop/yas3fs)) - Yet Another S3-backed File System, inspired by s3fs.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;96⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5🍴</code></b> [grippy/node-s3](https://github.com/grippy/node-s3)) - Node.js app to manage buckets.
* <b><code>&nbsp;&nbsp;2923⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;349🍴</code></b> [jubos/fake-s3 :fire::fire::fire::fire::fire:](https://github.com/jubos/fake-s3)) - Lightweight S3 clone that simulates most commands.
* <b><code>&nbsp;&nbsp;5570⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;535🍴</code></b> [kahing/goofys :fire::fire::fire::fire::fire:](https://github.com/kahing/goofys)) -  a Filey System for Amazon S3 written in Go.
* <b><code>&nbsp;&nbsp;1058⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;47🍴</code></b> [littlstar/s3renity :fire::fire::fire::fire:](https://github.com/littlstar/s3renity)) - Batch functions with concurrency control (each, map, reduce, filter, join)
* <b><code>&nbsp;&nbsp;&nbsp;771⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;450🍴</code></b> [marcel/aws-s3 :fire::fire::fire:](https://github.com/marcel/aws-s3)) - Ruby implementation of Amazon's S3 REST API.
* <b><code>&nbsp;&nbsp;&nbsp;243⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;54🍴</code></b> [mardix/flask-cloudy :fire::fire:](https://github.com/mardix/flask-cloudy)) - Flask extension.
* <b><code>&nbsp;&nbsp;&nbsp;292⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;89🍴</code></b> [MathieuLoutre/grunt-aws-s3 :fire::fire:](https://github.com/MathieuLoutre/grunt-aws-s3)) - Grunt plugin.
* <b><code>&nbsp;14817⭐</code></b> <b><code>&nbsp;&nbsp;1014🍴</code></b> [mickael-kerjean/filestash :fire::fire::fire::fire::fire:](https://github.com/mickael-kerjean/filestash)) - A modern web client for S3.
* <b><code>&nbsp;&nbsp;3509⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;754🍴</code></b> [minio/mc :fire::fire::fire::fire::fire:](https://github.com/minio/mc)) -  Minio Client for filesystem and cloud storage.
* <b><code>&nbsp;61310⭐</code></b> <b><code>&nbsp;&nbsp;8214🍴</code></b> [minio/minio :fire::fire::fire::fire::fire:](https://github.com/minio/minio)) - Object storage server compatible with S3.
* <b><code>&nbsp;&nbsp;&nbsp;162⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;73🍴</code></b> [mumrah/s3-multipart :fire:](https://github.com/mumrah/s3-multipart)) - Parallel upload/download to S3 via Python.
* <b><code>&nbsp;60461⭐</code></b> <b><code>&nbsp;&nbsp;5559🍴</code></b> [ncw/rclone :fire::fire::fire::fire::fire:](https://github.com/ncw/rclone)) - Rsync for various cloud storage providers such as S3.
* <b><code>&nbsp;&nbsp;&nbsp;168⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14🍴</code></b> [owocki/s3_disk_util :fire:](https://github.com/owocki/s3_disk_util)) - S3 Disk usage (du) utility.
* <b><code>&nbsp;&nbsp;4221⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;351🍴</code></b> [peak/s5cmd :fire::fire::fire:](https://github.com/peak/s5cmd)) - Fast S3 and local filesystem execution tool with wildcard and batch command support.
* <b><code>&nbsp;&nbsp;&nbsp;393⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;83🍴</code></b> [pgherveou/gulp-awspublish :fire::fire:](https://github.com/pgherveou/gulp-awspublish)) - Gulp plugin.
* <b><code>&nbsp;&nbsp;1141⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;180🍴</code></b> [rlmcpherson/s3gof3r :fire::fire::fire::fire:](https://github.com/rlmcpherson/s3gof3r)) - Fast, concurrent, streaming access, includes a CLI.
* <b><code>&nbsp;&nbsp;1460⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;64🍴</code></b> [s3git/s3git :fire::fire::fire::fire:](https://github.com/s3git/s3git)) - CLI tool that allows you to create a distributed, decentralized and versioned repository.
* <b><code>&nbsp;10016⭐</code></b> <b><code>&nbsp;&nbsp;1080🍴</code></b> [s3fs-fuse/s3fs-fuse :fire::fire::fire::fire::fire:](https://github.com/s3fs-fuse/s3fs-fuse)) - Allows Linux and Mac OS X to mount an S3 bucket via FUSE.
* <b><code>&nbsp;&nbsp;4920⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;904🍴</code></b> [s3tools/s3cmd :fire::fire::fire::fire::fire:](https://github.com/s3tools/s3cmd)) - CLI for managing S3 and CloudFront.
* <b><code>&nbsp;&nbsp;&nbsp;232⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;38🍴</code></b> [schickling/git-s3 :fire::fire:](https://github.com/schickling/git-s3)) - Deploy your git repo to a bucket.
* <b><code>&nbsp;&nbsp;&nbsp;416⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;107🍴</code></b> [sorentwo/carrierwave-aws :fire::fire:](https://github.com/sorentwo/carrierwave-aws)) - Adapter for CarrierWave.
* <b><code>&nbsp;&nbsp;&nbsp;215⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;169🍴</code></b> [spring-projects/aws-maven :fire::fire:](https://github.com/spring-projects/aws-maven)) -  Maven Wagon for S3.
* <b><code>&nbsp;&nbsp;&nbsp;136⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;32🍴</code></b> [tongwang/s3fs-c :fire:](https://github.com/tongwang/s3fs-c)) - Mounts buckets for use on a local file system.
* <b><code>&nbsp;&nbsp;&nbsp;317⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;99🍴</code></b> [mishudark/s3-parallel-put :fire::fire:](https://github.com/mishudark/s3-parallel-put)) - CLI that supports parallel uploads.
* <b><code>&nbsp;&nbsp;&nbsp;653⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;324🍴</code></b> [waynehoover/s3_direct_upload :fire::fire::fire:](https://github.com/waynehoover/s3_direct_upload)) - Direct Upload to Amazon S3 With CORS
* <b><code>&nbsp;&nbsp;&nbsp;202⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;102🍴</code></b> [weavejester/clj-aws-s3 :fire:](https://github.com/weavejester/clj-aws-s3)) - Client library for Clojure.

### SES

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;543⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;109🍴</code></b> [drewblas/aws-ses :fire::fire::fire:](https://github.com/drewblas/aws-ses)) - Provides an easy ruby DSL & interface.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [microapps/MoonMail :fire::fire::fire::fire:](https://github.com/microapps/MoonMail)) - Shoot billions of emails using SES and Lambda.

### Simple Workflow

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;134⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;59🍴</code></b> [aws-flow-ruby :fire:](https://github.com/aws/aws-flow-ruby)) - Creates background jobs and multistep workflows.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;66⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;24🍴</code></b> [aws-flow-ruby-samples](https://github.com/awslabs/aws-flow-ruby-samples)) - AWS Flow Framework for Ruby samples.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4🍴</code></b> [aws-flow-ruby-opsworks-helloworld](https://github.com/awslabs/aws-flow-ruby-opsworks-helloworld)) - Hello World sample.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### SimpleDB

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;133⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;21🍴</code></b> [rjrodger/simpledb :fire:](https://github.com/rjrodger/simpledb)) - Node.js library.

### SNS

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;218⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;59🍴</code></b> [aws-php-sns-message-validator :fire:](https://github.com/aws/aws-php-sns-message-validator)) - Message validation for PHP.

Community Repos:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### SQS

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;183⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;150🍴</code></b> [amazon-sqs-java-messaging-lib :fire:](https://github.com/awslabs/amazon-sqs-java-messaging-lib)) - Holds the Java Message Service to communicate with SQS.

Community Repos:

* <b><code>&nbsp;&nbsp;2127⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;286🍴</code></b> [phstc/shoryuken :fire::fire::fire::fire:](https://github.com/phstc/shoryuken)) - A super efficient SQS thread based message processor for Ruby.

### Data

AWS Repos:

* <b><code>&nbsp;&nbsp;4123⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;751🍴</code></b> [aws-data-wrangler :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-data-wrangler)) - Connects Pandas DataFrames and AWS data related services.

Community Repos:

* <b><code>&nbsp;29378⭐</code></b> <b><code>&nbsp;&nbsp;8005🍴</code></b> [donnemartin/data-science-ipython-notebooks :fire::fire::fire::fire::fire:](https://github.com/donnemartin/data-science-ipython-notebooks)) - Big data/data science notebooks.
* <b><code>&nbsp;&nbsp;&nbsp;428⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;134🍴</code></b> [everpeace/vagrant-mesos :fire::fire:](https://github.com/everpeace/vagrant-mesos)) - Spin up your Mesos Cluster with Vagrant.
* <b><code>&nbsp;&nbsp;&nbsp;253⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;25🍴</code></b> [jhorey/ferry :fire::fire:](https://github.com/jhorey/ferry)) -  Define, run, and deploy big data apps using Docker.
* <b><code>&nbsp;&nbsp;&nbsp;513⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;143🍴</code></b> [nathanmarz/storm-deploy :fire::fire::fire:](https://github.com/nathanmarz/storm-deploy)) - One click deploy for Storm clusters.

### DevOps

Community Repos:

* <b><code>&nbsp;&nbsp;6091⭐</code></b> <b><code>&nbsp;&nbsp;1671🍴</code></b> [cloud-custodian/cloud-custodian :fire::fire::fire::fire::fire:](https://github.com/cloud-custodian/cloud-custodian)) - Rules engine for management, DSL in yaml for query, filter, and actions on resources.
* <b><code>&nbsp;&nbsp;&nbsp;664⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;554🍴</code></b> [chef-cookbooks/aws :fire::fire:](https://github.com/chef-cookbooks/aws)) - Development repository for aws Chef cookbook.
* <b><code>&nbsp;&nbsp;1331⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;394🍴</code></b> [colinbjohnson/aws-missing-tools :fire::fire::fire::fire:](https://github.com/colinbjohnson/aws-missing-tools)) - Tools for managing resources including EC2, EBS, RDS and Route53.
* <b><code>&nbsp;&nbsp;1173⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;188🍴</code></b> [k1LoW/awspec :fire::fire::fire::fire:](https://github.com/k1LoW/awspec)) - RSpec tests your resources.
* <b><code>&nbsp;&nbsp;2584⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;565🍴</code></b> [mitchellh/vagrant-aws :fire::fire::fire::fire::fire:](https://github.com/mitchellh/vagrant-aws)) - Use Vagrant to manage your EC2 and VPC instances.
* <b><code>&nbsp;&nbsp;2211⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;363🍴</code></b> [NixOS/nixops :fire::fire::fire::fire:](https://github.com/NixOS/nixops)) - Use NixOS to provision EC2 instances, S3 buckets, and other resources.

### Security

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2🍴</code></b> [aws-sha256-agentcs](https://github.com/awslabs/aws-sha256-agentcs)) - SHA256 Agent Compatibility Ccanner.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;24🍴</code></b> [aws-tvm-anonymous](https://github.com/awslabs/aws-tvm-anonymous)) - Token Vending Machine for Anonymous Registration.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;38⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;18🍴</code></b> [aws-tvm-identity](https://github.com/awslabs/aws-tvm-identity)) - Token Vending Machine for Identity Registration.
* <b><code>&nbsp;&nbsp;4782⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;808🍴</code></b> [s2n :fire::fire::fire::fire::fire:](https://github.com/awslabs/s2n)) - An implementation of the TLS/SSL protocols.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;810⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;42🍴</code></b> [AdRoll/hologram :fire::fire::fire:](https://github.com/AdRoll/hologram)) - Easy, painless credentials on developer laptops.
* <b><code>&nbsp;&nbsp;&nbsp;727⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [alex/letsencrypt-aws :fire::fire::fire:](https://github.com/alex/letsencrypt-aws)) - Automatically provision and update certificates.
* <b><code>&nbsp;&nbsp;9090⭐</code></b> <b><code>&nbsp;&nbsp;1445🍴</code></b> [bridgecrewio/checkov :fire::fire::fire::fire::fire:](https://github.com/bridgecrewio/checkov)) - Terraform static analysis, verifies security best practices.
* <b><code>&nbsp;&nbsp;3783⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;751🍴</code></b> [cloudsploit/scans :fire::fire::fire::fire:](https://github.com/cloudsploit/scans)) - Detects security risks.
* <b><code>&nbsp;&nbsp;1718⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;284🍴</code></b> [iSECPartners/Scout2 :fire::fire::fire::fire:](https://github.com/iSECPartners/Scout2)) - Security auditing tool.
* <b><code>&nbsp;&nbsp;1471⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;245🍴</code></b> [jordanpotti/AWSBucketDump :fire::fire::fire::fire:](https://github.com/jordanpotti/AWSBucketDump)) - Security Tool to Look For Interesting Files in S3 Buckets.
* <b><code>&nbsp;&nbsp;2758⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;229🍴</code></b> [Netflix/bless :fire::fire::fire::fire::fire:](https://github.com/Netflix/bless)) - SSH Certificate Authority that runs as a Lambda function.
* <b><code>&nbsp;&nbsp;4371⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;774🍴</code></b> [Netflix/security_monkey :fire::fire::fire::fire::fire:](https://github.com/Netflix/security_monkey)) - Monitors policy changes and alerts on insecure configurations.
* <b><code>&nbsp;&nbsp;&nbsp;445⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;38🍴</code></b> [RiotGames/cloud-inquisitor :fire::fire:](https://github.com/RiotGames/cloud-inquisitor)) - Tool to enforce ownership and data security.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [salesforce/policy_sentry :fire::fire::fire::fire:](https://github.com/salesforce/policy_sentry/)) - IAM Least Privilege Policy Generator.
* <b><code>&nbsp;&nbsp;&nbsp;183⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [sebsto/AWSVPN :fire:](https://github.com/sebsto/AWSVPN)) - Start a private VPN server in the cloud.
* <b><code>&nbsp;30436⭐</code></b> <b><code>&nbsp;&nbsp;2369🍴</code></b> [trailofbits/algo :fire::fire::fire::fire::fire:](https://github.com/trailofbits/algo)) - Set up a personal IPSEC VPN on EC2 and other cloud services.
* <b><code>&nbsp;&nbsp;2017⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;134🍴</code></b> [ttlequals0/autovpn :fire::fire::fire::fire:](https://github.com/ttlequals0/autovpn)) - Create On Demand Disposable OpenVPN Endpoints.

### Accompanying Repos

AWS Repos:

*Repos Accompanying Blogs, Training Events, and Conferences.*

* <b><code>&nbsp;&nbsp;&nbsp;262⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;42🍴</code></b> [aws-arch-backoff-simulator :fire:](https://github.com/awslabs/aws-arch-backoff-simulator)) - Jitter and backoff Simulator for AWS architecture blog.
* <b><code>&nbsp;&nbsp;&nbsp;891⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;610🍴</code></b> [aws-big-data-blog :fire::fire::fire:](https://github.com/awslabs/aws-big-data-blog)) - Samples from the AWS Big Data Blog.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;54🍴</code></b> [aws-demo-php-simple-app](https://github.com/awslabs/aws-demo-php-simple-app)) - PHP apps from the AWS Blogs.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5🍴</code></b> [aws-mobile-sample-wif](https://github.com/awslabs/aws-mobile-sample-wif)) - Samples from the AWS Mobile SDK blog.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;15⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14🍴</code></b> [aws-mobile-self-paced-labs-samples](https://github.com/awslabs/aws-mobile-self-paced-labs-samples)) - Android Snake Game from a self-paced lab.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [aws-quickstart](https://github.com/aws-quickstart/)) - Official repository for AWS Quick Start.
* <b><code>&nbsp;&nbsp;&nbsp;984⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;314🍴</code></b> [aws-spot-labs :fire::fire::fire:](https://github.com/awslabs/aws-spot-labs)) - Best practices using AWS Spot Instances.
* <b><code>&nbsp;&nbsp;&nbsp;128⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;79🍴</code></b> [aws-training-demo :fire:](https://github.com/awslabs/aws-training-demo)) - Demos from the Technical Trainers community.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;56⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [java-meme-generator-sample](https://github.com/awslabs/java-meme-generator-sample)) - Meme generation app from re:Invent 2012.
* <b><code>&nbsp;&nbsp;&nbsp;165⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [railsconf2013-tech-demo :fire:](https://github.com/awslabs/railsconf2013-tech-demo)) - Seahorse demo from RailsConf 2013.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;15🍴</code></b> [reinvent2013-js-blog-demo](https://github.com/awslabs/reinvent2013-js-blog-demo)) - Demo blogging app from re:Invent 2013.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;23⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10🍴</code></b> [reinvent2013-mobile-photo-share](https://github.com/awslabs/reinvent2013-mobile-photo-share)) - Mobile photo share app from re:Invent 2014.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;53⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [reinvent2014-scalable-site-management](https://github.com/awslabs/reinvent2014-scalable-site-management)) - Scalable site management sample from re:Invent 2014.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2🍴</code></b> [reinvent2015-dev309](https://github.com/awslabs/reinvent2015-dev309)) - Large Scale Metrics Analysis from re:Invent 2015.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;29⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;13🍴</code></b> [timely-security-analytics](https://github.com/awslabs/timely-security-analytics)) - Security analytics sample from 2015 re:Invent 2015.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;28⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;50🍴</code></b> [todo-sample-app](https://github.com/awslabs/todo-sample-app)) - Simple "Todo" app from RailsConf 2014.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;294⭐</code></b> <b><code>&nbsp;&nbsp;1224🍴</code></b> [startup-class/setup :fire::fire:](https://github.com/startup-class/setup)) -  EC2 setup files for Startup Engineering MOOC.

### Miscellaneous Repos

AWS Repos:

* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;60⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;42🍴</code></b> [amediamanager](https://github.com/awslabs/amediamanager)) - Media manager.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;15⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [aws-hal-client-java](https://github.com/awslabs/aws-hal-client-java)) - Java client for the Hypertext Application Language.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;10🍴</code></b> [aws-model-validators](https://github.com/awslabs/aws-model-validators)) - Tools for validating the AWS service JSON model files.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;22⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;14🍴</code></b> [aws-sdk-js-sample-video-transcoder](https://github.com/awslabs/aws-sdk-js-sample-video-transcoder)) - Sample cross-platform video transcoder app.
* <b><code>&nbsp;&nbsp;&nbsp;317⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;71🍴</code></b> [simplebeerservice :fire::fire:](https://github.com/awslabs/simplebeerservice)) - Cloud-connected kegerator that streams live sensor data to AWS.

Community Repos:

* <b><code>&nbsp;&nbsp;&nbsp;440⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;64🍴</code></b> [bcoe/thumbd :fire::fire:](https://github.com/bcoe/thumbd)) - Node.js/ImageMagick-based image thumbnailing service.
* <b><code>&nbsp;&nbsp;2349⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;269🍴</code></b> [cdkpatterns/serverless :fire::fire::fire::fire:](https://github.com/cdk-patterns/serverless)) - Deployable serverless architecture patterns built in AWS CDK.
* <b><code>&nbsp;&nbsp;&nbsp;274⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;49🍴</code></b> [Comcast/cmb :fire::fire:](https://github.com/Comcast/cmb)) - Highly available, horizontally scalable queuing and notification service.
* <b><code>&nbsp;&nbsp;1891⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;177🍴</code></b> [convox/rack :fire::fire::fire::fire:](https://github.com/convox/rack)) - Open-source PaaS on AWS.
* <b><code>&nbsp;&nbsp;&nbsp;387⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;118🍴</code></b> [devops-israel/aws-inventory :fire::fire:](https://github.com/devops-israel/aws-inventory)) - Display all your AWS resources on a single web page.
* <b><code>&nbsp;&nbsp;6279⭐</code></b> <b><code>&nbsp;&nbsp;1135🍴</code></b> [donnemartin/dev-setup :fire::fire::fire::fire:](https://github.com/donnemartin/dev-setup)) - Mac setup of various developer tools and AWS services.
* <b><code>&nbsp;&nbsp;4248⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;628🍴</code></b> [dtan4/terraforming :fire::fire::fire::fire::fire:](https://github.com/dtan4/terraforming)) - Export existing resources to Terraform style (tf, tfstate).
* <b><code>&nbsp;&nbsp;2086⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;408🍴</code></b> [segmentio/stack :fire::fire::fire::fire::fire:](https://github.com/segmentio/stack)) - A set of Terraform modules for configuring production infrastructure.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0🍴</code></b> [j2labs/microarmy ](https://github.com/j2labs/microarmy)) - Deploy micro instances to launch a coordinated siege.
* <b><code>&nbsp;&nbsp;&nbsp;171⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;43🍴</code></b> [jpillora/grunt-aws :fire:](https://github.com/jpillora/grunt-aws)) - Grunt interface into the Node.JS SDK.
* <b><code>&nbsp;&nbsp;&nbsp;279⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;62🍴</code></b> [jvehent/haproxy-aws :fire::fire:](https://github.com/jvehent/haproxy-aws)) - Documentation on building a HTTPS stack with HAProxy.
* <b><code>&nbsp;65141⭐</code></b> <b><code>&nbsp;&nbsp;4806🍴</code></b> [localstack/localstack :fire::fire::fire::fire::fire:](https://github.com/localstack/localstack)) - A fully functional local AWS cloud stack. Develop and test your cloud apps offline!
* <b><code>&nbsp;&nbsp;&nbsp;312⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [meducation/propono :fire::fire:](https://github.com/meducation/propono)) - Easy-to-use pub/sub in Ruby.
* <b><code>&nbsp;&nbsp;&nbsp;806⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;76🍴</code></b> [mozilla/awsbox :fire::fire::fire:](https://github.com/mozilla/awsbox)) - A featherweight PaaS on top of EC2 for deploying node apps.
* <b><code>&nbsp;&nbsp;&nbsp;957⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;167🍴</code></b> [Netflix/aminator :fire::fire::fire:](https://github.com/Netflix/aminator)) - A tool for creating EBS AMIs.
* <b><code>&nbsp;&nbsp;2498⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;475🍴</code></b> [Netflix/archaius :fire::fire::fire::fire::fire:](https://github.com/Netflix/archaius)) - Library for configuration management API.
* <b><code>&nbsp;&nbsp;2225⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;389🍴</code></b> [Netflix/asgard :fire::fire::fire::fire::fire:](https://github.com/Netflix/asgard)) - Web interface for application deployments and cloud management.
* <b><code>&nbsp;&nbsp;&nbsp;419⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;83🍴</code></b> [Netflix/aws-autoscaling :fire::fire:](https://github.com/Netflix/aws-autoscaling)) - Tools for using auto scaling and documentation best practices.
* <b><code>&nbsp;17183⭐</code></b> <b><code>&nbsp;&nbsp;1307🍴</code></b> [Netflix/chaosmonkey :fire::fire::fire::fire::fire:](https://github.com/Netflix/chaosmonkey)) - Resiliency tool that helps applications tolerate random instance failures.
* <b><code>&nbsp;12750⭐</code></b> <b><code>&nbsp;&nbsp;3759🍴</code></b> [Netflix/eureka :fire::fire::fire::fire::fire:](https://github.com/Netflix/eureka)) - Service registry for resilient mid-tier load balancing and failover.
* <b><code>&nbsp;&nbsp;2226⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;254🍴</code></b> [Netflix/EVCache :fire::fire::fire::fire:](https://github.com/Netflix/EVCache)) - A distributed in-memory data store.
* <b><code>&nbsp;&nbsp;&nbsp;698⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;113🍴</code></b> [Netflix/Fenzo :fire::fire::fire:](https://github.com/Netflix/Fenzo)) - Extensible Scheduler for Mesos Frameworks.
* <b><code>&nbsp;&nbsp;2876⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;423🍴</code></b> [Netflix/ice :fire::fire::fire::fire::fire:](https://github.com/Netflix/ice)) - Usage and cost monitoring tool.
* <b><code>&nbsp;&nbsp;4614⭐</code></b> <b><code>&nbsp;&nbsp;1222🍴</code></b> [Netflix/ribbon :fire::fire::fire::fire::fire:](https://github.com/Netflix/ribbon)) - Remote procedure call library with built in software load balancers.
* <b><code>&nbsp;&nbsp;7975⭐</code></b> <b><code>&nbsp;&nbsp;1113🍴</code></b> [Netflix/SimianArmy :fire::fire::fire::fire::fire:](https://github.com/Netflix/SimianArmy)) - Tools to keep your cloud operating in top form.
* <b><code>&nbsp;14093⭐</code></b> <b><code>&nbsp;&nbsp;2442🍴</code></b> [Netflix/zuul :fire::fire::fire::fire::fire:](https://github.com/Netflix/zuul)) - Edge service that provides dynamic routing, monitoring, resiliency, security, and more.
* <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [niftylettuce/gulp-aws-splash :fire::fire:](https://github.com/niftylettuce/gulp-aws-splash)) - Open-source LaunchRock alternative. Build beautiful splash pages.
* <b><code>&nbsp;&nbsp;&nbsp;186⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;210🍴</code></b> [puppetlabs/puppetlabs-aws :fire:](https://github.com/puppetlabs/puppetlabs-aws)) - Puppet module for managing resources to build out infrastructure.
* <b><code>&nbsp;&nbsp;&nbsp;297⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;43🍴</code></b> [mhart/react-server-routing-example :fire::fire:](https://github.com/mhart/react-server-routing-example)) - Sample universal client/server routing and data in React.
* <b><code>&nbsp;&nbsp;&nbsp;733⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;60🍴</code></b> [Similarweb/finala :fire::fire::fire:](https://github.com/similarweb/finala)) - A resource cloud scanner that analyzes and reports wasteful and unused resources to cut unwanted expenses.
* <b><code>&nbsp;&nbsp;7044⭐</code></b> <b><code>&nbsp;&nbsp;1171🍴</code></b> [snowplow/snowplow :fire::fire::fire::fire::fire:](https://github.com/snowplow/snowplow)) - Enterprise-strength web, mobile and event analytics, powered by Hadoop, Kafka, Kinesis, Redshift and Elasticsearch.
* <b><code>&nbsp;&nbsp;9814⭐</code></b> <b><code>&nbsp;&nbsp;1279🍴</code></b> [Spinnaker/spinnaker :fire::fire::fire::fire::fire:](https://github.com/Spinnaker/spinnaker)) - Successor to asgard supporting pipelines and more.
* <b><code>&nbsp;&nbsp;8717⭐</code></b> <b><code>&nbsp;&nbsp;2285🍴</code></b> [spulec/moto :fire::fire::fire::fire::fire:](https://github.com/spulec/moto)) - Allows your python tests to easily mock out the boto library.

## Guides, Books, Documentation, and Training

*How-to's, training, whitepapers, docs, and case studies.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/LxYDN5K.png">
</p>
<br/>

### Getting Started Guides

AWS Guides:

* [Getting Started with AWS](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-intro.html)
* [Getting Started Tutorials](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html)
    * [Run a Virtual Server](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2614)
    * [Store Files](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2683)
    * [Share Digital Media](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2755)
    * [Deploy a Website](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2767)
    * [Host a Website (Linux)](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2836)
    * [Host a Website (Windows)](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2908)
    * [Run a Database](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2980)
    * [Analyze Your Data](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e3065)

Community Guides:

* [Contribute](https://github.com/correia-jpv/fucking-awesome-aws/blob/master/CONTRIBUTING.md)

### General Guides

AWS Guides:

* 🌎 [Analyzing Big Data](docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
* [Working with the AWS Management Console](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html)
* [Deploying a Web App Using Elastic Beanstalk](http://docs.aws.amazon.com/gettingstarted/latest/deploy/overview.html)
* [Hosting a Web App](http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/web-app-hosting-intro.html)
* [Hosting a .NET Web App](http://docs.aws.amazon.com/gettingstarted/latest/wah/web-app-hosting-intro.html)
* [Hosting a Static Website](http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html)
* 🌎 [Quick Start Deployment Guides](aws.amazon.com/documentation/quickstart/)

Community Guides:

* <b><code>&nbsp;36465⭐</code></b> <b><code>&nbsp;&nbsp;3876🍴</code></b> [Open Guide to AWS :fire::fire::fire::fire::fire:](https://github.com/open-guides/og-aws))

### Books

* Amazon Web Services in Action 🌎 [Manning](www.manning.com/books/amazon-web-services-in-action) or [Amazon.com](http://amzn.com/1617292885)
* AWS Lambda in Action 🌎 [Manning](www.manning.com/books/aws-lambda-in-action) or [Amazon.com](http://amzn.com/1617293717) - <b><code>&nbsp;&nbsp;&nbsp;288⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [Code Repo :fire::fire:](https://github.com/danilop/AWS_Lambda_in_Action))

### Whitepapers

* 🌎 [AWS Well-Architected Framework](d0.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)
* 🌎 [Whitepapers](aws.amazon.com/whitepapers/)

### Documentation

* 🌎 [Documentation](aws.amazon.com/documentation/)
* 🌎 [AWS Billing and Cost Management](aws.amazon.com/documentation/account-billing/)
* 🌎 [AWS Marketplace](aws.amazon.com/documentation/marketplace/)
* 🌎 [AWS Support](aws.amazon.com/documentation/aws-support/)
* [AWS General Reference](http://docs.aws.amazon.com/general/latest/gr/)
* [AWS Glossary](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

### Training

* 🌎 [Training and Certification](aws.amazon.com/training/)
* 🌎 [Webinars](aws.amazon.com/about-aws/events/)

### Case Studies: Powered by AWS

* 🌎 [Adobe](aws.amazon.com/solutions/case-studies/adobe/)
* 🌎 [AdRoll](aws.amazon.com/solutions/case-studies/adroll/)
* 🌎 [Airbnb](aws.amazon.com/solutions/case-studies/airbnb/)
* 🌎 [Autodesk](aws.amazon.com/solutions/case-studies/autodesk/)
* 🌎 [Citrix](aws.amazon.com/solutions/case-studies/citrix/)
* 🌎 [Comcast](aws.amazon.com/solutions/case-studies/comcast/)
* 🌎 [Coursera](aws.amazon.com/solutions/case-studies/coursera/)
* 🌎 [Docker](aws.amazon.com/solutions/case-studies/docker/)
* 🌎 [Dow Jones](aws.amazon.com/solutions/case-studies/dow-jones/)
* 🌎 [Dropbox](www.dropbox.com/)
* 🌎 [Dropcam](aws.amazon.com/solutions/case-studies/dropcam/)
* 🌎 [Expedia](aws.amazon.com/solutions/case-studies/expedia/)
* 🌎 [Foursquare](aws.amazon.com/solutions/case-studies/foursquare/)
* 🌎 [IMDb](aws.amazon.com/solutions/case-studies/imdb/)
* 🌎 [Instrumental](instrumentalapp.com/blog/aws-kinesis/)
* 🌎 [Intuit](aws.amazon.com/solutions/case-studies/soasta-intuit/)
* 🌎 [Johnson & Johnson](aws.amazon.com/solutions/case-studies/johnson-and-johnson/)
* 🌎 [Lionsgate](aws.amazon.com/solutions/case-studies/lionsgate/)
* 🌎 [mlbam](a