# Schemas
An AI agent has at least one schema. Each schema define:
- an input structure
- an output structure

For example, a [task that answer question about a PDF](https://workflowai.dev/workflowai/tasks/pdf-question-answering/1/schemas) is represented:
![alt text](assets/Screenshot 2025-01-03 at 15.16.32.png)

And in Python:
{% hint style="info" %}
WorkflowAI uses [Pydantic](https://docs.pydantic.dev/) to define schemas.
{% endhint %}
```python
class PdfQuestionAnsweringTaskInput(BaseModel):
    pdf_document: Optional[File] = None
    question: Optional[str] = None

class SupportingQuote(BaseModel):
    quote: Optional[str] = None
    page_number: Optional[float] = None

class PdfQuestionAnsweringTaskOutput(BaseModel):
    answer: Optional[str] = None
    supporting_quotes: Optional[list[SupportingQuote]] = None
```

## Why are schemas a good idea?
Clear input and output structures (=schemas) have a few benefits:
1. simplify integration with a backend by providing a clear interface
2. provide output consistency
3. increase the quality of LLM outputs by structuring the task

### Technical details
WorkflowAI leverages structured generation, also called [structured output](https://platform.openai.com/docs/guides/structured-outputs), or [controlled generation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output). Structured generation is currently enabled for [all supported OpenAI models](https://platform.openai.com/docs/guides/structured-outputs), and for all models on [Fireworks](https://docs.fireworks.ai/structured-responses/structured-response-formatting#structured-response-modes). When structured generation is not available, WorkflowAI automatically falls back to [JSON mode](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency), and **always guarantees** the output will follow the output schema.


## How to create a schema?
WorkflowAI supports two ways to create a task schema:
- using our web-app, using AI or manually. 
- using code, via Cursor.

[video]

## Edit a schema
Finding the right schema takes a few iterations, so we try to make editing a schema as easy as possible.

[video]

When possible, we recommend to edit the schema using the chat. If you need more control, you can manually edit the schema.

## Archiving a schema
When building a new task, it's very likely you'll need multiple iterations to get the right schema. To clean up unused schemas, you can archive them.

To archive a schema, navigate to the "Schemas" section from the menu, and click on the "Archive" button in the schema's detail view.

![alt text](assets/Screenshot 2025-01-03 at 16.04.38.png)
[video]

{% hint style="important" %}
Archived schemas are not deleted, but hidden from the UI. Any deployment or version using an archived schema will continue to work, to avoid breaking changes.
{% endhint %}