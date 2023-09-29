# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .chat_completion_role import ChatCompletionRole

__all__ = ["ChatCompletionChunk", "Choice", "ChoiceDelta", "ChoiceDeltaFunctionCall"]


class ChoiceDeltaFunctionCall(BaseModel):
    arguments: Optional[str] = None
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Optional[str] = None
    """The name of the function to call."""


class ChoiceDelta(BaseModel):
    content: Optional[str] = None
    """The contents of the chunk message."""

    function_call: Optional[ChoiceDeltaFunctionCall] = None
    """
    The name and arguments of a function that should be called, as generated by the
    model.
    """

    role: Optional[ChatCompletionRole] = None
    """The role of the author of this message."""


class Choice(BaseModel):
    delta: ChoiceDelta
    """A chat completion delta generated by streamed model responses."""

    finish_reason: Optional[Literal["stop", "length", "function_call", "content_filter"]]
    """The reason the model stopped generating tokens.

    This will be `stop` if the model hit a natural stop point or a provided stop
    sequence, `length` if the maximum number of tokens specified in the request was
    reached, `content_filter` if content was omitted due to a flag from our content
    filters, or `function_call` if the model called a function.
    """

    index: int
    """The index of the choice in the list of choices."""


class ChatCompletionChunk(BaseModel):
    id: str
    """A unique identifier for the chat completion chunk."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion chunk was created."""

    model: str
    """The model to generate the completion."""

    object: str
    """The object type, which is always `chat.completion.chunk`."""