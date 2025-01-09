## What are AI agents?

AI agents are mini-programs that are using AI algorithms (LLMs) to perform intelligent operations. For example, a AI agent can:
- summarize a text [todo: add link to public task]
- browse a company URL to extract the list of customers [todo: add link to public task]
- generate SOAP notes from a medical report [todo: add link to public task]
- search the web to answer a question [todo: add link to public task]
- generate product descriptions from images [todo: add link to public task]
- [add more examples, link]

AI agents can access tools, some of which are built-in, like searching the web, navigating on webpages, or your own custom tools.
By combining agents, you can create [complex workflows](link).

## What are some great use-cases for AI agents?
The easiest way to get started with a personalized list of AI agents for your product and company is to go to [workflowai.com](https://workflowai.com) and enter your company URL.

## What use-cases are not well supported (yet!)?
Currenytly, WorkflowAI agents are not able to:
- generate images, but they can understand images as inputs
- listen and participate in real-time audio conversations, but they can understand audio files as inputs
- TODO: your own custom tools (subscribe to this discussion on GH https://github.com/WorkflowAI/WorkflowAI/discussions/categories/ideas)

WorkflowAI does not currently support the following features:
- fine-tuning and distillation, but you can export the outputs of an agent from WorkflowAI and use them in your own fine-tuning pipeline
- RAG is not directly supported, but [WorkflowAI can be integrated with your own RAG pipeline](). 

{% hint style="info" %}
We expect that all these uses will be supported in the future (by end of 2025).
{% endhint %}

WorkflowAI is open-source, if you like to contribute to these new use-cases, please open a PR or a discussion on GitHub. https://github.com/workflowai/workflowai