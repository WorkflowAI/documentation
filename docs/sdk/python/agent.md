# How `@agent` works

An agent is composed of three parts:

1. Schema (input, output)
2. Instructions
3. Model

Optionally, an agent can also have tools, which will be explained in the [Tools](sdk/python/tools.md) section.

## Schema (input, output)

The schema has two structured parts:

| | |
|------|-------------|
| Input | Defines the variables that the agent will receive as input |
| Output | Defines the variables that the agent will return as output |

The input and output are defined using [Pydantic](https://docs.pydantic.dev/latest/) models.

A very simple example of a schema is the following:

```python
from pydantic import BaseModel

class Input(BaseModel):
    question: str

class Output(BaseModel):
    answer: str
```

### Descriptions

Adding descriptions to the input and output models is optional, but it's a good practice to do so, as descriptions will be included in the final prompt sent to the LLM. And so, it's a good way to align the agent's behavior.

```python
class Input(BaseModel):
    question: str

class Output(BaseModel):
    answer: str = Field(description="Answer with bullet points.")
```

### Examples

Another effective way to align the agent's behavior is to provide examples for **output** models.

```python
class Output(BaseModel):
    answer: str = Field(
        description="Answer with bullet points.",
        examples=[
            "- Answer 1",
            "- Answer 2", 
            "- Answer 3"
        ]
    )
```

Note that adding examples to **input** models is not helpful.

## Instructions

Instructions are helpful for the agent to understand the task it needs to perform. Use docstring to add instructions to the agent.

```python
@workflowai.agent()
async def answer_question(input: Input) -> Output:
    """
    You are an expert in history.
    Answer the question with attention to detail and historical accuracy.
    """
    ...
```

## Model

The model is the LLM that will be used to generate the output. WorkflowAI offers a unified interface for all the models it supports from OpenAI, Anthropic, Google, and more. Simply pass the model you want to use to the `model` parameter.

{% hint style="info" %}
The [list of models supported by WorkflowAI is available here](https://github.com/WorkflowAI/workflowai-py/blob/main/workflowai/core/domain/model.py), but you can also see the list of models from the playground, for a more user-friendly experience.
{% endhint %}

```python
import workflowai
from workflowai import Model

@workflowai.agent(model=Model.GPT_4O_LATEST)
async def answer_question(input: Input) -> Output:
    ...
```

## Running the agent

To run the agent, simply call the agent function with an input.

```python
run = await answer_question(Input(question="What is the history of Paris?"))
print(run)

# - Paris, originally a settlement of the Parisii tribe, was established around 250 BC on the Île de la Cité.
# - The Romans conquered the area in 52 BC, renaming it Lutetia, and later Paris, as it became a significant city in the Roman Empire.
# - During the Middle Ages, Paris grew as a center of learning and culture, with the founding of the University of Paris in 1150.
# ...
```

### Override the default model

You can also pass a `model` parameter to the agent function itself to specify the model you want to use, and override the default model set in the `@agent` decorator.

```python
run = await answer_question(
    Input(question="What is the history of Paris?"),
    model=Model.CLAUDE_3_5_SONNET_LATEST
)
print(run)
```

### Cost, latency

WorkflowAI automatically tracks the cost and latency of each run, and makes it available in the `run` object.

To access the cost and latency, you need to use the `Run` class.

```python
from workflowai import Model, Run

@workflowai.agent(model=Model.CLAUDE_3_5_SONNET_LATEST)
# The return type is a Run[Output]
async def answer_question(input: Input) -> Run[Output]:
    ...

run = await answer_question(Input(question="What is the history of Paris?"))
print(f"Cost: $ {run.cost_usd}")
print(f"Latency: {run.duration_seconds:.2f}s")

# Cost: $ 0.007266000000000001
# Latency: 8.70s
```

### Streaming

```python
from collections.abc import AsyncIterator

@workflowai.agent(model=Model.CLAUDE_3_5_SONNET_LATEST)
# no need to mark the function as async since it returns an AsyncIterator
def answer_question_stream(input: Input) -> AsyncIterator[Output]:
    ...

async for chunk in answer_question_stream(Input(question="What is the history of Paris?")):
    print(chunk.answer)
```

{% hint style="info" %}
No need to mark the agent as async here ! It is already asynchronous since it returns an AsyncIterator.

The type checkers some times get confused since they consider that an async function that returns an AsyncIterator is async twice.

For example, a function with the signature `async def foo() -> AsyncIterator[int]` may be called `async for c in await foo():...` in certain cases...
{% endhint %}