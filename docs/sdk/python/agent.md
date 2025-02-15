# How `@workflowai.agent` works

An agent is composed of three parts:

1. Schema (input, output)
2. Instructions
3. Model

Optionally, an agent can also have tools, which will be explained in the [Tools](sdk/python/tools.md) section.

## Schema (input, output)

The schema has two structured parts:

| | |
|------|-------------|
| **Input** | Defines the variables that the agent will receive as input |
| **Output** | Defines the variables that the agent will return as output |

The input and output are defined using [Pydantic](https://docs.pydantic.dev/latest/) models.

A very simple example of a schema is the following, where the agent receives a question as input and returns an answer as output.

```python
from pydantic import BaseModel

class Input(BaseModel):
    question: str

class Output(BaseModel):
    answer: str
```

{% hint style="success" %}
Read more about why schemas are a good idea in the [Schemas](../../concepts/schemas.md#why-are-schemas-a-good-idea) section.
{% endhint %}

### Descriptions

Adding descriptions to the input and output fields is optional, but it's a good practice to do so, as descriptions will be included in the final prompt sent to the LLM. And so, it's a good way to align the agent's behavior.

```python
class Input(BaseModel):
    question: str

class Output(BaseModel):
    answer: str = Field(description="Answer with bullet points.")
```

### Examples

Another effective way to align the agent's behavior is to provide examples for **output** fields.

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

{% hint style="info" %}
There are very little use cases for descriptions and examples in the **input** fields. The LLM will most of the time infer from the value that is passed.
{% endhint %}

### Required versus optional fields

In short, we recommend using default values for most output fields.

Pydantic is by default rather strict on model validation. If there is no default value, the field must be provided.
Although the fact that a field is required is passed to the model, the generation can sometimes omit null or empty
values.

## Instructions

Instructions are helpful for the agent to understand the task it needs to perform. Use docstring to add instructions to the agent.

```python
@workflowai.agent(id="answer-question")
async def answer_question(input: Input) -> Output:
    """
    You are an expert in history.
    Answer the question with attention to detail and historical accuracy.
    """
    ...
```

Instructions are automatically passed to the LLM via the system prompt.

```
system_prompt = """<instructions>You are an expert in history. Answer the question with attention to detail and historical accuracy.</instructions>"""
```

### Variables in instructions

You can customize your agent's instructions using [Jinja2](https://jinja.palletsprojects.com/) template variables in the docstring. These variables are automatically filled with values from your input model's fields, giving you precise control over the final prompt.

```python
class Input(BaseModel):
    question: str
    word_count: int

class Output(BaseModel):
    answer: str

@workflowai.agent(id="answer-question-with-word-count", model=Model.CLAUDE_3_5_HAIKU_LATEST)
async def answer_question(input: Input) -> Output:
    """
    The answer should be less than {{ word_count }} words.
    Answer the following question:
    {{ question }}
    """
    ...

# Run the agent
run = await answer_question.run(
    Input(
        question="What is artificial intelligence?",
        word_count=5
    )
)

# View prompt
# https://workflowai.com/docs/agents/answer-question-with-word-count/1/runs?page=0&taskRunId=019509ed-017e-7059-4c25-6137ebdb7dcd
# System prompt:
# <instructions>The answer should be less than 5 words. Answer the following question: What is artificial intelligence?</instructions>
# { "answer": "Smart computer systems learning" }
```

{% hint style="warning" %}
Custom Jinja2 Template Tags Being Incorrectly Rendered as GitBook Custom Blocks
{% endhint %}

<details>
<summary>Example: Code Review Agent</summary>

```python
class CodeReviewInput(BaseModel):
    language: str = Field(description="Programming language of the code")
    style_guide: str = Field(description="Style guide to follow")
    is_production: bool = Field(description="Whether this is a production review")
    focus_areas: list[str] = Field(description="Areas to focus on during review", default_factory=list)

class CodeReviewOutput(BaseModel):
    """Output from a code review."""
    issues: list[str] = Field(
        default_factory=list,
        description="List of identified issues or suggestions for improvement"
    )
    compliments: list[str] = Field(
        default_factory=list,
        description="List of positive aspects and good practices found in the code"
    )
    summary: str = Field(
        description="A brief summary of the code review findings"
    )

@workflowai.agent(id="code-review")
async def review_code(review_input: CodeReviewInput) -> CodeReviewOutput:
    """
    You are a code reviewer for {{ language }} code.
    Please review according to the {{ style_guide }} style guide.

    {% if is_production %}
    This is a PRODUCTION review - be extra thorough and strict.
    {% else %}
    This is a development review - focus on maintainability.
    {% endif %}

    {% if focus_areas %}
    Key areas to focus on:
    {% for area in focus_areas %}
    {{ loop.index }}. {{ area }}
    {% endfor %}
    {% endif %}
    """
    ...
```

</details>

{% hint style="info" %}
We recommend using CursorAI, Claude or ChatGPT to help generate the Jinja2 template.

The template uses [Jinja2](https://jinja.palletsprojects.com/) syntax and supports common templating features including:

- Variable substitution: `{{ variable }}`
- Conditionals: `{% if condition %}...{% endif %}`
- Loops: `{% for item in items %}...{% endfor %}`
- Loop indices: `{{ loop.index }}`

See the [Jinja2 documentation](https://jinja.palletsprojects.com/) for the full template syntax and capabilities.
{% endhint %}

### Temperature

The temperature is a parameter that controls the randomness of the output. It is a float between 0 and 1. The default temperature is 0.

```python
run = await answer_question.run(
    Input(question="What is the history of Paris?"),
    temperature=0.5
)
```

## Model

The model is the LLM that will be used to generate the output. WorkflowAI offers a unified interface for all the models it supports from OpenAI, Anthropic, Google, and more. Simply pass the model you want to use to the `model` parameter.

{% hint style="info" %}
The [list of models supported by WorkflowAI is available here](https://github.com/WorkflowAI/workflowai-py/blob/main/workflowai/core/domain/model.py), but you can also see the list of models from the playground, for a more user-friendly experience.
{% endhint %}

Set the model in the `@agent` decorator.

```python
import workflowai
from workflowai import Model

@workflowai.agent(id="answer-question", model=Model.GPT_4O_LATEST)
async def answer_question(input: Input) -> Output:
    ...
```

{% hint style="info" %}
When a model is retired, it will be replaced dynamically by a newer version of the same model with the same or a lower price so using a model is always guaranteed to work in the future.
{% endhint %}

## Running the agent

{% hint style="warning" %}
Before you run the agent, make sure you have [setup the WorkflowAI client](./get-started.md#api-key).
{% endhint %}

To run the agent, simply call the `run` function with an input.

```python
run = await answer_question.run(Input(question="What is the history of Paris?"))
print(run)

# Output:
# ==================================================
# {
#   "answer": "- Paris, the capital of France, has a history that dates back to ancient times, originally settled by the Parisii, a Celtic tribe, around 250 BC.\n- During the Roman era, it was known as Lutetia and became a significant city in the Roman province of Gaul.\n- In the Middle Ages, Paris grew as a center of learning and culture, with the establishment of the University of Paris in the 12th century.\n- The city played a pivotal role during the French Revolution in the late 18th century, becoming a symbol of revolutionary ideals.\n- In the 19th century, Paris underwent major transformations under Baron Haussmann, who modernized the city's infrastructure and architecture.\n- Paris was occupied during World War II but was liberated in 1944, marking a significant moment in its modern history.\n- Today, Paris is renowned for its cultural heritage, iconic landmarks like the Eiffel Tower and Notre-Dame Cathedral, and its influence in art, fashion, and politics."
# }
# ==================================================
# Cost: $ 0.0027
# Latency: 6.54s
```

When you call `run`, the associated agent will be created on WorkflowAI Cloud (or your self-hosted server) if it does not already exist.

{% hint style="info" %}
The agent id will be a slugified version of the function name unless specified explicitly using the `id` parameter, which is **recommended**.

```python
@workflowai.agent(id="answer-question")
async def answer_question(input: Input) -> Output:
    ...
```
{% endhint %}

### Override the default model

You can also pass a `model` parameter to the agent function itself to specify the model you want to use, and override the default model set in the `@agent` decorator.

```python
run = await answer_question.run(
    Input(question="What is the history of Paris?"),
    model=Model.CLAUDE_3_5_SONNET_LATEST
)
print(run)
```

### Cost, latency

WorkflowAI automatically tracks the cost and latency of each run, and makes it available in the `run` object.

```python
run = await answer_question.run(Input(question="What is the history of Paris?"))
print(f"Cost: $ {run.cost_usd:.5f}")
print(f"Latency: {run.duration_seconds:.2f}s")

# Cost: $ 0.00745
# Latency: 8.99s
```

### Streaming

WorkflowAI also support streaming the output, using the `stream` method. The `stream` method returns an AsyncIterator, so you can use it in an async for loop.

```python
async for chunk in answer_question.stream(Input(question="What is the history of Paris?")):
    print(chunk)

# Output:
# ==================================================
# {
#   "answer": "-"
# }
# ==================================================

# Output:
# ==================================================
# {
#   "answer": "- Founde"
# }
# ==================================================

# Output:
# ==================================================
# {
#   "answer": "- Founded aroun"
# }
# ==================================================

# Output:
# ==================================================
# {
#   "answer": "- Founded around 250"
# }
# ==================================================

# Output:
# ==================================================
# {
#   "answer": "- Founded around 250 BCE"
# }
# ==================================================
# ...
```

{% hint style="info" %}
Even when using streaming, partial outputs are returned as valid output schemas.
{% endhint %}

### Error handling

Read more about error handling in the [Errors](./errors.md) section.

### Cache

To save money and improve latency, WorkflowAI supports caching.

By default, the cache settings is `auto`, meaning that agent runs are cached when the temperature is 0
(the default temperature value) and no tools are used. Which means that, when running the same agent (without tools) twice with the **exact** same input, the exact same output is returned and the underlying model is not called a second time.

The cache usage string literal is defined in [cache_usage.py](https://github.com/WorkflowAI/workflowai-py/blob/main/workflowai/core/domain/cache_usage.py) file. There are 3 possible values:

- `auto`: (default) Use cached results only when temperature is 0, and no tools are used
- `always`: Always use cached results if available, regardless of model temperature
- `never`: Never use cached results, always execute a new run

```python
# Never use cache
run = agent.run(input, use_cache='never')

# Always use cache
run = agent.run(input, use_cache='always')

# Auto (default): use cache when temperature is 0 and no tools are used
run = agent.run(input)
```