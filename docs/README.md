# Twitter::Account::Tweet

An example resource schema demonstrating some basic constructs and validation rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Twitter::Account::Tweet",
    "Properties" : {
        "<a href="#accesskey" title="accessKey">accessKey</a>" : <i>String</i>,
        "<a href="#secretkey" title="secretKey">secretKey</a>" : <i>String</i>,
        "<a href="#consumeraccesskey" title="consumerAccessKey">consumerAccessKey</a>" : <i>String</i>,
        "<a href="#consumersecretkey" title="consumerSecretKey">consumerSecretKey</a>" : <i>String</i>,
        "<a href="#tweet" title="tweet">tweet</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Twitter::Account::Tweet
Properties:
    <a href="#accesskey" title="accessKey">accessKey</a>: <i>String</i>
    <a href="#secretkey" title="secretKey">secretKey</a>: <i>String</i>
    <a href="#consumeraccesskey" title="consumerAccessKey">consumerAccessKey</a>: <i>String</i>
    <a href="#consumersecretkey" title="consumerSecretKey">consumerSecretKey</a>: <i>String</i>
    <a href="#tweet" title="tweet">tweet</a>: <i>String</i>
</pre>

## Properties

#### accessKey

Access key for interacting with twitter apis

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### secretKey

Secret key for interacting with twitter apis

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### consumerAccessKey

Secret key for interacting with twitter apis

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### consumerSecretKey

Secret key for interacting with twitter apis

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### tweet

Tweet to post

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tweetId.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tweetId

tweet identifier

