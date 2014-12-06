#!/usr/bin/python

# Import troposphere
from troposphere import Template, Ref, Output, Join, GetAtt, Parameter
import troposphere.ec2 as ec2

# Create a template for resources to live in
template = Template()

keypair = template.add_parameter(Parameter(
    "KeyPair",
    Type="String",
    Description="The name of the keypair to use for SSH access",
))

# Create a security group
sg = ec2.SecurityGroup('MySecurityGroup')
sg.GroupDescription = "Allow access to MyInstance"
sg.SecurityGroupIngress = [
    ec2.SecurityGroupRule(
        IpProtocol="tcp",
        FromPort="22",
        ToPort="22",
        CidrIp="0.0.0.0/0",
    )]

# Add security group to template
template.add_resource(sg)

# Create an instance
instance = ec2.Instance("MyInstance")
instance.ImageId = "ami-ef277b86"
instance.InstanceType = "t1.micro"
instance.SecurityGroups = [Ref(sg)]
instance.KeyName = Ref(keypair)

# Add instance to template
template.add_resource(instance)

# Add output to template
template.add_output(Output(
    "InstanceAccess",
    Description="Command to use to SSH to instance",
    Value=Join("", ["ssh -i ", Ref(keypair), " ubuntu@", GetAtt(instance, "PublicDnsName")])
))

# Print out CloudFormation template in JSON
print template.to_json()
