# `@prompt`

{% hint style="info" %}
This feature is only available via the Python SDK for now.
{% endhint %}

## What is `@prompt`?

`@prompt` allows you to write a prompt fully customizable, using code, and still benefit from the WorkflowAI platform.

```python
@prompt(name='answer_question', model='gpt-4o-mini')
def prompt(question: str) -> str:
    system("You are a helpful assistant that can answer questions about the world.")
    user(question)
```

## When to use `@prompt` vs `@agent`? 

## Tools

## Structured output

## Supported features

### Playground
Supported, but instructions should be left empty.

### Benchmarks
Currently not supported for `@prompt`.

### Deployments
Currently not supported for `@prompt`.
