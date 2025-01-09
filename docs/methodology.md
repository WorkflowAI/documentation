# Methodology

Developing great AI agents is a process of iterations.
Based on our experience with customers building AI agents and deploying them to production, WorkflowAI has developed a methodology to help you, step-by-step.

WorkflowAI has been designed both for developers and non-developers.

## First POC of your agent, in a few minutes.
The goal is to set something running quickly, a POC (Proof of Concept) to validate that AI is able to do what you want, without aiming for perfect results all the time, but getting a first feel of what is possible, or not.

To create a first version of a new agent, you'll need to be able to describe in a few sentences what the agent should do.

{% hint style="info" %}
We recommend starting using the web-app, as it's the fastest way to get started.
{% endhint %}

### New AI agent
Tap "+ New AI agent" on the web-app, then write a few sentences describing what the agent should do. 

### A first schema
A schema is a definition of the (input, output) of your agent. For example, if you want an agent to summarize a text, the input is a text, and the output is a summary. If you want the agent to summarize a text in a language that is dependent on the context, you'll need to add a language parameter to the input. The input is like all the variables the LLM will have access to. The output is the different fields the LLM will generate.

WorkflowAI will automatically generate a first schema based on your description. 

{% hint style="info" %}
Don't focus about the first schema being perfect, you'll likely iterate on the schema multiple times. WorkflowAI handles very well multiple schemas per AI agent, so you can easily edit the schema later.
{% endhint %}

Once you're happy with your first schema, tap "Save and Try in Playground".

### Run the first agent
You have two options to run your agent:
#### Playground (web-app)

#### Code

Congratulations, your AI agent is running! Now you can iterate on it.

## Iterate
The playground (on the web-app) is where you can iterate on your agent quickly.

### Descriptions
The first step is to make sure the descriptions are clear and complete. Descriptions are helping the LLM to understand what the input and the output are. WorkflowAI will use AI to generate the descriptions, but you can also edit them manually.

### Examples (for output)
Examples are very powerful way to help the LLM understand what the output should look like.

### Models
Get a first feel of what models are performing well, and don't hesitate to try multiple models.

#### Test with more inputs


## Improve the agent

There can be a few reasons why the agent is not performing well. 
You need to identify the root cause, and make some changes accordingly. We've listed the most common reasons below.

### The schema misses some *input* parameters
Example: a task where a transcript of a discussion is extracting calendar events, but the input is missing the `transcript_time` parameter.

Solution: edit the schema. You can edit the schema via WorkflowAI web-app, or via code directly.

### The schemas misses some *output* parameters
Example: a task where a transcript of a discussion is extracting calendar events, but the output is missing the `event_time` parameter.

Solution: edit the schema. You can edit the schema via WorkflowAI web-app, or via code directly.

### The agent is not able to access the tools it needs.
Example: if you ask a LLM a question after its training date, without including any @search tool.

Solution: add the tools to the agent.

### the (input, output) context window is maxed out.
Example: if you a ask a LLM to ...

Solution, try a model with larger context window, or reduce the size of the input and output.

### The instructions are invalid, ambiguous, incomplete..
Example: a task that summarize a text, the user wants bullet points summary, but the instructions are not mentioning this requirement. 

Solution: write feedback, test a new prompt.

### Examples and descriptions are not precise.

### The task is too difficult for some models.

Solution: try a different model, more intelligent. 

### The task is too difficult for all models.
Example: if you ask a LLM to solve a hypothesis still unsolved in math.

{% hint style="info" %}
Make sure you've tested the most intelligent models available.
{% endhint %}


Solution: in that case, you'll need to re-evaluate what your AI agent can do.