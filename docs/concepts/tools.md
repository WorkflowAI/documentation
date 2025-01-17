# Tools
## What are tools?
Tools enable tasks to access external services, like searching the web, navigating on webpages, executing code and running other functions.

Tools have two forms:
| **Function Calling** | Developer-defined code.                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------|
| **Hosted Tools**      | WorkflowAI-built tools (e.g., *search*, *browser-text*).

## Hosted Tools

### What hosted tools are available?
WorklfowAI supports and manages the following tools:
- `@search`: search the web to answer a question
- `@browser-text`: navigate on webpages (text-only)

We're working on adding more tools, if you need any specfic tool, please open a discussion on [GitHub](https://github.com/workflowai/workflowai/discussions/categories/ideas) or contact us on [Slack](https://workflowai.com/slack).

### How to enable tools?

[todo: explain how to enable tools]
From the playground, under "Instructions", tap on the tools you want to enable.

[image]

### How are tools billed?
Tools are billed independently from the LLM inference costs.
- `@search` tool: $0.... per search
- `@browser-text` tool: $0.... per webpage

## Function Calling

[todo: explain how to use function calling]

