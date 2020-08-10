import logging
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
)
import twitter

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Twitter::Account::Follow"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    client = create_twitter_client(model)

    # Example:
    try:
        status = client.PostUpdate(model.tweet)
        progress.status = OperationStatus.SUCCESS
    except TypeError as e:
        # exceptions module lets CloudFormation know the type of failure that occurred
        raise exceptions.InternalFailure(f"was not expecting type {e}")
        # this can also be done by returning a failed progress event
        # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")
    model.consumerSecretKey = None
    model.consumerAccessKey = None
    model.accessKey = None
    model.secretKey = None
    model.tweetId = str(status.id)

    return progress




@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    client = create_twitter_client(model)

    client.DestroyStatus(model.tweetId)
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )
    # TODO: put code here
    return progress


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState

    client = create_twitter_client(model)
    status = client.GetStatus(model.tweetId)
    model.tweet = status.text
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )

def create_twitter_client(model):
    return twitter.Api(consumer_key=model.consumerAccessKey,
                         consumer_secret=model.consumerSecretKey,
                         access_token_key=model.accessKey,
                         access_token_secret=model.secretKey)
