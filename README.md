# WorkflowAI
WorkflowAI is an open-source platform for building AI-first products and companies.

[todo: add license badge]

Tasks – our first primitive – enable simple yet powerful "AI functions". For example, a AI task can:
- summarize a text [todo: add link to public task]
- browse a company URL to extract the list of customers [todo: add link to public task]
- search the web to answer a question [todo: add link to public task]
- [add more examples, link]

## Demo
> Build your first task in less than [todo: update] minutes:

[embedded .mp4]

## Features
WorkflowAI facilitates the complete lifecycle of building with AI, encompassing all stages from initial prototyping and development to deployment in production and ongoing continuous improvement, including:

- Playground: Compare models side-by-side, iterate on prompts, and save different versions.
- Versions: List all task versions and archive those that are no longer in use.
- Schemas: Define and manage the input and output structures for your tasks.
- Runs: View all executions of a task and search for specific runs.
- Code: Copy the generated code to seamlessly integrate tasks into your codebase.
- Deployments: Deploy specific versions of a task with ease, allowing for updates to prompts and models without any code changes.
- Monitor: Track usage metrics and monitor the costs associated with task executions.

# Introduction

## Tasks

### What is a task?
A task is like a function in programming, but instead of executing deterministic code, a task leverages Large Language Models (LLMs) to perform intelligent operations. Tasks are the building blocks for creating AI-powered features, and building AI-first products and companies.

#### What is the difference between a task and a LLM prompt?
A LLM prompt is a text that describe the task. A task is a concept that includes:
- a notion of input and output
- a ...


#### What are great use-cases for task?
The easiest way to get started with a personalized list of tasks for your product and company: [workflowai.com](https://workflowai.com)

Examples:
- [summarize a text](https://workflowai.com/tasks/summarize-a-text)
- [browse a company URL to extract the list of customers](https://workflowai.com/tasks/browse-company-url-extract-customers)
- [search the web to answer a question](https://workflowai.com/tasks/search-web-answer-question)
- ...

#### What use-cases are not well supported (yet!)?

- (check chatbot)
- image generation
- audio real-time (see OpenAI's [real-time speech-to-text API](https://platform.openai.com/docs/guides/realtime))
- custom tools (subscribe to this discussion on GH https://github.com/WorkflowAI/WorkflowAI/discussions/categories/ideas)
- agents (subscribe to this discussion on GH https://github.com/WorkflowAI/WorkflowAI/discussions/categories/ideas)

We expect that all these uses will be supported in the future (by end of 2025). 

> WorkflowAI is open-source, if you like to contribute to these new use-cases, please open a PR or a discussion on GitHub. https://github.com/workflowai/workflowai
> We're also hiring – join our distributed team. https://workflowai.com/jobs

## Schemas
A task has at least one schema. Each schema define:
- an input structure
- an output structure

For example, a [task that answer question about a PDF](https://workflowai.dev/workflowai/tasks/pdf-question-answering/1/schemas) is represented:
![alt text](<Screenshot 2025-01-03 at 15.16.32.png>)

And in Python:
> WorkflowAI uses [Pydantic](https://docs.pydantic.dev/) to define schemas.
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

@workflowai.task(schema_id=1, version=1)
async def pdf_question_answering(task_input: PdfQuestionAnsweringTaskInput) -> Run[PdfQuestionAnsweringTaskOutput]:
    ...
```

#### Why are schemas a good idea?
Clear input and output structures (=schemas) have a few benefits:
1. simplify integration with a backend by providing a clear interface
2. provide output consistency
3. increase the quality of LLM outputs by structuring the task

##### Technical details
WorkflowAI leverages structured generation, also called [structured output](https://platform.openai.com/docs/guides/structured-outputs), or [controlled generation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output). Structured generation is currently enabled for [all supported OpenAI models](https://platform.openai.com/docs/guides/structured-outputs), and for all models on [Fireworks](https://docs.fireworks.ai/structured-responses/structured-response-formatting#structured-response-modes). When structured generation is not available, WorkflowAI automatically falls back to [JSON mode](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency), and **always guarantees** the output will follow the schema.


#### How to create a task schema?
WorkflowAI supports two ways to create a task schema:
- using AI, of course!
- manually, for more advanced use-cases.

#### Edit a task schema
Finding the right schema takes a few iterations, so we try to make editing a schema as easy as possible. 

[video]

When possible, we recommend to edit the schema using the chat. If you need more control, you can manually edit the schema.

#### Archiving a schema
When building a new task, it's very likely you'll need multiple iterations to get the right schema. To clean up unused schemas, you can archive them.

To archive a schema, navigate to the "Schemas" section from the menu, and click on the "Archive" button in the schema's detail view.

![alt text](<Screenshot 2025-01-03 at 16.04.38.png>)
[video]

Important: Archived schemas are not deleted, but hidden from the UI. Any deployment or version using an archived schema will continue to work, to avoid breaking changes.

## Versions
WorkflowAI defines two types of (task) versions:

[todo: add screenshot]

- **Minor Versions** (e.g., 1.1, 1.2, 1.3, ...)

  A minor version represents a specific implementation of a task, including its prompt and the specific model used (e.g., OpenAI's GPT-4o-mini).

- **Major Versions** (e.g., 1, 2, 3, ...)
  
  A major version groups multiple minor versions together, all sharing the same prompt.


#### Saving versions
When using the playground, you can save a version by clicking on the "Save" button. Additionnaly, you can save all versions by clicking on the "Save all versions" button.

#### When to save a version?
You should save a version when you're satisfied with the LLM output and want to preserve the current configuration. A saved version captures your chosen model, prompt, temperature setting, and other parameters, allowing you to reliably reproduce these results later, or use them in a [deployment](/deployments).

#### List of all versions
You can access the list of all versions by clicking on the "Versions" section from the menu.
[video]

## Playground
[todo: add screenshot]
![alt text](<Screenshot 2025-01-03 at 15.28.30.png>)

Playground is designed to iterate quickly on prompts and models. By default, you can compare 3 models side-by-side.

The playground is composed of 3 sections:
- **Input**: where the input variables are defined.
- **Parameters**: where the prompt and temperature are defined.
- **Outputs**: where the LLM outputs are displayed.

### Input
You can manually enter the input variable, and for text inputs (only), you can use AI to generate synthetic data.

[video]

### Parameters
You can adjust the prompt and temperature.

#### Prompt
The prompt is the text of instructions given to the LLM to perform the task.

When you create a new task, WorkflowAI will generate a default prompt for you. You can manually edit the prompt to customize the task, but our recommanded approach is to use the [AI prompt engineering](/prompt-engineering) feature to improve the prompt.

#### Temperature
Temperature is a parameter that controls the randomness of the LLM's outputs. WorkflowAI provides three preset temperature settings: [todo: check if smart default temperature per task type is rolled out https://linear.app/workflowai/issue/WOR-681/[plan]-suggest-the-right-temperature-for-the-task]

- **Precise** (Default): The recommended and default setting for all tasks
  - Best for tasks requiring accuracy and consistency
  - Ideal for factual responses, code generation, or structured data extraction
  - Produces reliable, repeatable results

- **Balanced**: Moderate setting that balances creativity and coherence
  - Good for general-purpose tasks
  - Works well for most conversational and analytical tasks
  - Provides reasonable variation while maintaining relevance

- **Creative**: Maximum diversity and exploration
  - Best for tasks requiring unique or innovative outputs
  - Ideal for brainstorming, creative writing, or generating alternatives
  - Produces more varied but potentially less focused results
- **Custom**: User-defined temperature setting
  - Allows precise control over the temperature value
  - For advanced users who understand the impact of temperature

Note: "Precise" is automatically selected as the default temperature setting for all new tasks to ensure consistent and reliable outputs. You can adjust this in the Parameters section of the Playground if your use case requires more variation.

[video]

### Outputs
The outputs section displays the LLM outputs.

[video]

For each output, WorkflowAI also displays:
- 💰 Cost: The total price in USD for generating this output
- ⚡ Latency: How long it took to get a response from the model, in seconds
- 📊 Context window usage: How much of the model's maximum token limit was used, shown as a percentage

> WorkflowAI Cloud offers a price-match guarantee, meaning that you're not charged more than the price per token of the model you're using. Learn more about the price-match guarantee [here](https://workflowai.com/pricing).

![alt text|300](<Screenshot 2025-01-03 at 15.52.23.png>)

### Pro-tip
You can display 1, 2, or 3 model outputs side-by-side in the playground to focus on a single output, compare two options, or evaluate multiple variations simultaneously.

### Diff mode
You can enable diff mode to highlight the differences between LLM outputs, making it easy to spot exactly what words or sections changed between different outputs.

[video]

![alt text](<Screenshot 2025-01-03 at 15.47.42.png>)

## Runs
A run is a single execution of a task. By default, WorkflowAI stores all runs, available in the "Runs" section.

![alt text](<Screenshot 2025-01-03 at 17.04.12.png>)

### Why storing all runs?
- **Observability**: Understand how the AI is performing by tracking and analyzing its outputs over time.
- **Saving cost**: For the same input and model versions, cached runs can be served without triggering a new LLM call, reducing costs to $0 for serving cached runs.
- **Fine-Tuning and distillation**: Saving all runs is required for fine-tuning models and distillation processes.

### How to search runs?
WorkflowAI provides a powerful search – available under the "Runs" section – to find specific runs:

![alt text](<Screenshot 2025-01-03 at 17.11.48.png>)

> Architecture: under the hood, runs are stored in a Clickhouse database, which is optimized for handling large amount of data, and for fast search and aggregation queries. Clickhouse also compresses data, which reduces storage costs. Learn more about Clickhouse [here](https://clickhouse.com/docs/en/introduction).

## Code
### How to integrate a task in your codebase?

## Reliability
[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v2/monitor/1cuxx.svg)](https://status.workflowai.com)

Our goal with WorkflowAI Cloud is to provide a 100% uptime on our API endpoint that is used for running a task.

We've designed our architecture to be resilient. 

[todo: explain more about provider fallback and Azure multi-region]

## Deployments
Deploy specific versions of a task with ease, allowing for updates to prompts and models without any code changes.

### Why use deployments?
- ✅ update to a new model or prompt without asking your engineering team.
- ✅ save cost by updating to a more recent, cheaper model, without changing your code.
- ✅ improve the quality of your tasks outputs by adjusting the prompt, in real-time, based on users' feedback.
- ✅ use different versions of a task in different environments (development, staging, production).

### How to deploy a version?
[video]
- Go to "Deployments" section from the menu.
- Pick the environment you want to deploy to, either: production, staging, or development.
- Tap [Deploy Version]
- Select the version you want to deploy.
- Tap [Deploy]

> To avoid any breaking changes: deployments are **schema specific**, meaning that you can deploy a (development, staging, production) version for each schema of a task.

### Using your own AI Providers API
#### When to use your own API key?
- if you have custom data-retention agreement.
 - if you have credits from [Microsoft Startups](https://startups.microsoft.com/), [Google AI credits](https://cloud.google.com/startup), or [Amazon Bedrock credits](https://aws.amazon.com/startups/credits).
- if you want to use your own rate limits.

Remember that WorkflowAI Cloud offers a price-match guarantee, meaning that you're not charged more than the price per token of the model you're using. Learn more about the price-match guarantee [here](https://workflowai.com/pricing).

### How to use your own API key?
- Go to "Deployments" section from the menu.
- Tap [Manage Provider Keys]
- Select the provider you want to use.
- Enter your API key.
- Tap [Save]

> Security: when using WorkflowAI Cloud, your API keys are encrypted at rest. 

When you're using our own API keys, WorkflowAI Cloud will not charge you for the LLM calls or storage of runs, but you might get charged for other features (tools like `web-search` and `browser-text` for example).

## Compliance
### No training on your data, ever.
We have contractual agreements with our AI subprocessors that prohibit the use of customer data to train their models.

### SOC2 (Type1) Compliance

> Report is available [here](https://workflowai.com/docs/soc2-report.pdf).

WorkflowAI Cloud is SOC2 Type1 compliant, ensuring that our platform meets rigorous security and compliance standards. This certification verifies the design and implementation of our security controls at a specific point in time, covering the following principles:

- **Security:** Protecting against unauthorized access (both physical and logical).
- **Availability:** Ensuring that the system is available for operation and use as committed.
- **Processing Integrity:** Guaranteeing that system processing is complete, valid, accurate, timely, and authorized.
- **Confidentiality:** Maintaining the confidentiality of information as committed or agreed.
- **Privacy:** Protecting personal information according to the commitments in the privacy notice.

Achieving SOC2 Type1 compliance demonstrates our commitment to maintaining the highest standards of security and operational excellence, providing our users with confidence in the integrity and reliability of our services.

> If you have specific compliance questions and requirements (HIPPA, GDPR, data retention, etc), please contact us at [compliance@workflowai.com](mailto:compliance@workflowai.com).

## Monitoring
...


## Advanced use-cases
### Workflows
Workflows are a way to chain tasks together, and to add conditional logic.

### RAG (Retrieval-Augmented Generation)
#### What is RAG?
RAG is a technique to improve the quality of LLM outputs by adding relevant information from a knowledge base.

## ...
WorkflowAI enables 

- AI-agent: chat with AI to create a task.
- Playground: compare models side-by-side.

WorkflowAI includes:
- a web app to [create task](link), [compare models side-by-side](link), [iterate on prompts](link), [version prompts](link), benchmarks versions, monitor cost.
- a API container that serves as a [high-avaibility inference proxy]([todo: add link to documentation]). 
- a storage layer to store all LLM outputs (called runs). 

## AI-first
(todo: write definition) 

## Get started
The easiest way to get started is to enter your company URL on [workflowai.com](https://workflowai.com),
and get a [todo: improve this copy]personalized list of AI-powered tasks to improve your product and company in a few seconds[/todo.

### WorkflowAI Cloud
[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v2/monitor/1cuxx.svg)](https://status.workflowai.com)

WorkflowAI as a service, fully-managed and [effectively free](todo: add link). 
[Get started with $10 of free LLM credits.](https://workflowai.com/)

### Self-Hosting
```
# Clone repository
todo: complete instructions

# Run server and database
docker compose up -d
```

## Roadmap
- Evaluations: compare how different prompts and models are performing, using a built-in AI agent. 
- Tools: enable tasks to access tools, like searching the web, navigating on webpages, executing code and running other functions. 
- Multimodal Capabilities: currently, WorkflowAI supports audio and image as input. We’re working on supporting audio and image as output as well, and real-time API for conversations. 
- Fine-Tuning & Model Distillation: [Tailor models to your data for unmatched performance.] (to be rewrote) 
- Autonomous Agents: Build agents to automate entire workflows.

If you would like to contribute, please:
- [Open a PR](https://github.com/workflowai/workflowai/pulls)
- [Open a discussion](https://github.com/workflowai/workflowai/discussions)

You can also join our [Slack](https://workflowai.com/slack) chat with WorkflowAI team and other users.

## Useful Links
* [WorkflowAI Cloud](https://workflowai.com/) WorkflowAI as a service, built by the creators and maintainers.
* [Documentation](todo: add link) on how to use WorkflowAI platform. 
* [Slack](https://workflowai.com/slack) chat with WorkflowAI team and other users.
* [X](https://x.com/withworkflowai) 
