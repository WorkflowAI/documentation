# Advanced workflows

https://www.anthropic.com/research/building-effective-agents 

## Workflow: Parallelization
LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

Sectioning: Breaking a task into independent subtasks run in parallel.
Voting: Running the same task multiple times to get diverse outputs.

[how to build with WorkflowAI]

> https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/basic_workflows.ipynb

## Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

> https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/basic_workflows.ipynb

## Workflow: Orchestrator-workers
In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

## Workflow: Evaluator-optimizer
In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

## Fine-tuning

## RAG
