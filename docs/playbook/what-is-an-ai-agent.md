## What is an AI agent?

> The unprecedented capabilities of foundation models have opened the door to agentic applications that were previously unimaginable. These new capabilities make it finally possible to develop autonomous, intelligent agents to act as our assistants, coworkers, and coaches. They can help us create a website, gather data, plan a trip, do market research, manage a customer account, automate data entry, prepare us for interviews, interview our candidates, negotiate a deal, etc. The possibilities seem endless, and the potential economic value of these agents is enormous.
> [Chip Huyen](https://huyenchip.com/2025/01/07/agents.html)

AI agents are mini-programs that use AI algorithms (LLMs) as their brain to accomplish tasks typically provided by users or other agents. The AI agent understands the task requirements, plans a sequence of actions to achieve the task, executes the actions, and determines whether the task has been successfully completed.

For example, a AI agent can:
- summarize a text [todo: add link to public task]
- browse a company URL to extract the list of customers [todo: add link to public task]
- generate SOAP notes from a medical report [todo: add link to public task]
- search the web to answer a question [todo: add link to public task]
- generate product descriptions from images [todo: add link to public task]
- extract structured data from a PDF, image [todo: add link to public task]
- classify a customer message into a category [todo: add link to public task]
- scrape a listing website to extract structured data [todo: add link to public task]
- [add more examples, link]

AI agents can access [tools](#tools), some of which are built-in, like searching the web, navigating on webpages, or your own custom tools. The success of an agent depends on both the tools available to it and the capabilities of its AI planner.

<details>
<summary>REAL-LIFE EXAMPLE</summary>

Apple recently introduced a AI agent that can rewrite a text with a different tone.

[image]
</details>

### What AI Agents can you leverage?

The easiest way to get started with a personalized list of AI agents for your product and company is to go to [workflowai.com](https://workflowai.com) and enter your company URL.

WorkflowAI will generate a list of AI agents that are most likely to be useful for your company.

<details>
<summary>INSIDE WORKFLOWAI'S OWN AGENTS</summary>
When you use our feature that generates a list of AI agents from a company URL, under the hood, we're using 2 agents:
- a first [agent](https://workflowai.com/agents/1) is generating a profile of the company, by searching the web, and browsing the company website.
- a second [agent](https://workflowai.com/agents/2) is generating a list of AI agents that are most likely to be useful for your company.
</details>

<details>
<summary>REAL-LIFE AGENT</summary>
Berrystreet.co, a company that ..., developed a AI agent that can write SOAP notes from a medical report, using WorkflowAI, and deployed it to production. Since then, the agent has been used to generate over 1000 SOAP notes. 

[image]

</details>

### Tools

Let's look at why tools are so important through a simple example:

Web browsing was one of the first major tools added to ChatGPT. Without it, ChatGPT could only access information from its training data, which becomes outdated quickly. It couldn't tell you today's weather, recent news, upcoming events, or real-time stock prices. Web browsing keeps the agent current and vastly more useful.

This illustrates a key point: while an AI agent can function without external tools (like an LLM generating text), tools dramatically expand what an agent can do. Tools enable agents to perceive and interact with their environment in ways that would otherwise be impossible.

When designing an agent, carefully consider what tools to provide:
- More tools expand the agent's capabilities
- But too many tools can make it harder for the agent to be effective
- Finding the right balance requires experimentation

Common categories of tools include:

1. Knowledge augmentation tools (for building context)
   - Web search to get current information
   - Document retrieval from company knowledge bases
   - Database queries to access structured data

2. Capability extension tools
   - Image generation and analysis
   - Text-to-speech and speech-to-text conversion
   - Code execution and debugging
   - Language translation

3. Environment interaction tools
   - API calls to external services
   - Web browser automation
   - File system operations
   - Email and messaging integrations

{% hint style="info" %}
The tools you give an agent will determine what it can accomplish. We'll cover tool selection strategy later in the playbook.
{% endhint %}



