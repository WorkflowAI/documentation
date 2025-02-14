# Versions

WorkflowAI agents are versioned automatically.

To show how versions work, let's create a new agent that can triage a customer question into different categories.

```python
from typing import Literal
from pydantic import BaseModel
import workflowai

class Input(BaseModel):
    question: str

class Output(BaseModel):
    category: Literal["billing", "technical", "account", "other"]

@workflowai.agent(id="triage-agent")
async def triage_question(input: Input) -> Output:
    """
    Triage a customer question into different categories.
    """
    ...

await triage_question.run(Input(question="How do I change my billing information?"))
```

Running this agent for the first time will automatically create a new version of the agent on WorkflowAI.

You can also see the versions in the WorkflowAI dashboard.

> https://workflowai.com/docs/agents/triage-agent/1/versions

![Versions](/docs/assets/images/agents/triage-agent/version-1.png)

A version is a specific **configuration** of an agent.

WorkflowAI defines two types of (agent) versions:

| Version Type | Example | Description |
|--------------|---------|-------------|
| **Major** Versions | 1, 2, 3, ... | A major version represents a specific configuration of a agent, including its instructions, temperature, descriptions/examples, and tools. |
| **Minor** Versions | 1.1, 1.2, 1.3, ... | A minor version represents a major version **associated with a specific model** (e.g., OpenAI's GPT-4o-mini). |

Now let's create another version of the agent, but this time we'll use a different model.

```python
@workflowai.agent(
    id="triage-agent",
    model=Model.CLAUDE_3_5_HAIKU_LATEST
)
async def triage_question(input: Input) -> Output:
    """
    Triage a customer question into different categories.
    """
    ...

await triage_question.run(Input(question="How do I change my billing information?"))
```

This will create a new minor version of the agent associated with the `CLAUDE_3_5_HAIKU_LATEST` model.

![Versions](/docs/assets/images/agents/triage-agent/version-1.2.png)

## Major Versions

Major versions are created when you change the instructions, temperature, descriptions/examples, or tools of an agent.

For example, let's change the instructions of the agent.

```python
async def triage_question(input: Input) -> Output:
    """
    Triage a customer question into different categories.

    Categories:
    - billing: Questions about payments, invoices, pricing, or subscription changes
    - technical: Questions about API usage, SDK implementation, or technical issues
    - account: Questions about account access, settings, or profile management
    - other: Questions that don't fit into the above categories
    """
    ...
```

{% hint style="info" %}
Changelog between major versions will be generated automatically.
{% endhint %}

![Version 2 with new instructions](/docs/assets/images/agents/triage-agent/version-2.png)

## Versions from code, version id, or a deployment

WorkflowAI allows you to refer to a version of an agent from your code, a version id, or a deployment.

### Versions from code

Setting a docstring or a model in the agent decorator signals the client that the agent parameters are fixed and configured via code.

### Versions from version id

Since WorkflowAI automatically saves all versions, you can refer to a version by its id.

```python
@workflowai.agent(id="triage-agent", version="2.1")
```

{% hint style="info" %}
Find the exact code from WorkflowAI Code section.
> https://workflowai.com/docs/agents/triage-agent/1/code?selectedLanguage=Python
{% endhint %}

### Versions from a deployment

To learn more about deployments, read the [Deployments](/docs/features/deployments) section first.

Deployments allow you to refer to a version of an agent's parameters from your code that's managed from WorkflowAI dashboard. The following code will use the version of the agent named "production" which is a lot more flexible than changing the function parameters when running in production.

```python
@workflowai.agent(deployment="production") # or simply @workflowai.agent()
```