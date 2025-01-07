## Versions
WorkflowAI defines two types of (agent) versions:

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

#### Clone a version
[explain how to clone a version -- and why it's useful]