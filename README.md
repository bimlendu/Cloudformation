Cloudformation
==============

Cloudformation templates


* Using aws command line tools.

```Bimlendus-MacBook-Pro:~ bimlendu$ aws cloudformation create-stack --stack-name testing005 --template-body file:///Users/bimlendu/Desktop/Cloudformation/ELB.template.json --parameters ParameterKey=ELBDNSName,ParameterValue=testing005 ParameterKey=ELBName,ParameterValue=testing005 ParameterKey=HostedZone,ParameterValue=hubzu-test.com --profile hubzudev
{
    "StackId": "arn:aws:cloudformation:us-east-1:293713961925:stack/testing005/b97fef60-7d81-11e4-80d7-5001a7da7436"
}```
