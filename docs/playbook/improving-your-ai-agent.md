# Improve the agent
> This step can be done by either product or development team.

## Common issues

There can be a few reasons why the agent is not performing well. 
You need to identify the root cause, and make some changes accordingly. We've listed the most common reasons below.

### The schema misses some *input* parameters
Example: a task where a transcript of a discussion is extracting calendar events, but the input is missing the `transcript_time` parameter.

Solution: edit the schema. You can edit the schema via WorkflowAI web-app, or via code directly.

[expandable]
- edit via web-app
- edit via code
[end]

### The schemas misses some *output* parameters
Example: a task where a transcript of a discussion is extracting calendar events, but the output is missing the `event_time` parameter.

Solution: edit the schema. You can edit the schema via WorkflowAI web-app, or via code directly.

[expandable]
- edit via web-app
- edit via code
[end]

### The agent is not able to access the tools it needs.
Example: if you ask a LLM a question after its training date, without including any @search tool.

Solution: add the tools to the agent.

[expandable]
- edit via web-app
- edit via code
[end]

### the (input, output) context window is maxed out.
Example: if you a ask a LLM to ...

Solution, try a model with larger context window, or reduce the size of the input and output.

### The instructions are invalid, ambiguous, incomplete..
Example: a task that summarize a text, the user wants bullet points summary, but the instructions are not mentioning this requirement. 

Solution: write feedback, test a new prompt.

<details>
<summary>INSIDE WORKFLOWAI'S OWN AGENTS</summary>
When you use our feature that re-write the instructions bsaed on feedback, you're using a this [agent](https://workflowai.com/agents/1).
</details>

### Examples and descriptions are not precise.

### The task is too difficult for some models.

Solution: try a different model, more intelligent. 

### The task is too difficult for all models.
Example: if you ask a LLM to solve a hypothesis still unsolved in math.

{% hint style="info" %}
Make sure you've tested the most intelligent models available.
{% endhint %}

Solution: in that case, you'll need to re-evaluate what your AI agent can do.