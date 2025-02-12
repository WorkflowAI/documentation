# Get started

## Install the SDK

{% hint style="info" %}
`workflowai` requires Python >= 3.9.
{% endhint %}

[![PyPI version](https://img.shields.io/pypi/v/workflowai.svg)](https://pypi.org/project/workflowai/)

```sh
pip install workflowai
```

## API Key

Get your API key from your [WorkflowAI Cloud dashboard](https://workflowai.com/organization/settings/api-keys) or from your self-hosted WorkflowAI dashboard.

Set the `WORKFLOWAI_API_KEY` environment variable.

## Initialize the SDK

```python
import os
import workflowai

workflowai.init(
    api_key=os.environ.get("WORKFLOWAI_API_KEY"),  # This is the default and can be omitted
    base_url="https://run.workflowai.com",  # This is the default and can be omitted
)
```

{% hint style="info" %}
You can also set the `WORKFLOWAI_API_URL` environment variable to point to your self-hosted WorkflowAI.
{% endhint %}

## Write your first agent

An agent is in essence an async function with the added constraints that:

- it has a single argument that is a Pydantic model, which is the input to the agent
- it has a single return value that is a Pydantic model, which is the output of the agent
- it is decorated with the `@workflowai.agent()` decorator

{% hint style="info" %}
[Pydantic](https://docs.pydantic.dev/latest/) is a very popular and powerful library for data validation and parsing.
{% endhint %}

The following agent, given a city, returns the country, capital, and a fun fact about the city.

```python
import workflowai
from pydantic import BaseModel
from workflowai import Model

class CityInput(BaseModel):
    city: str

class CapitalOutput(BaseModel):
    country: str
    capital: str 
    fun_fact: str

@workflowai.agent()
async def get_capital_info(city_input: CityInput) -> CapitalOutput:
    ...
```
{% tabs %}

{% tab title="OpenAI" %}
```python
output = await get_capital_info(CityInput(city="New York"), model=Model.GPT_4O_LATEST)
print(output)

# country='United States'
# capital='Washington, D.C.'
# fun_fact="New York City is known as 'The Big Apple' and is famous for its cultural diversity and iconic landmarks like the Statue of Liberty and Times Square."
```
{% endtab %}

{% tab title="Anthropic" %}
```python
output = await get_capital_info(CityInput(city="New York"), model=Model.CLAUDE_3_5_SONNET_LATEST)
print(output)

# country='United States'
# capital='Washington, D.C.'
# fun_fact="New York City's Federal Reserve Bank has the largest gold storage in the world, containing approximately 7,000 tons of gold bullion stored 80 feet below street level."
```
{% endtab %}

{% tab title="Gemini" %}
```python
agent_output = await get_capital_info(CityInput(city="New York"), model=Model.GEMINI_2_0_FLASH_LATEST)
print(agent_output)

# country='United States of America'
# capital='Washington, D.C.'
# fun_fact='New York City is home to over 8 million people and over 800 languages are spoken in New York City, making it the most linguistically diverse city in the world.'
```
{% endtab %}

{% endtabs %}

So simple. And the agent created by the SDK is also available in the <a href="https://workflowai.com/docs/agents/get-capital-info" target="_blank">Playground</a>.