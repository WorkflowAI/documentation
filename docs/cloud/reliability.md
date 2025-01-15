## Reliability
[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v2/monitor/1cuxx.svg)](https://status.workflowai.com)

Our goal with WorkflowAI Cloud is to provide a 100% uptime on our API endpoint that is used for running an AI agent.

We've designed our architecture to be resilient in a few ways:
- at the AI provider level, we implemented a fallback mechanism that brings redundacy. For example, if OpenAI API is down, WorkflowAI will automatically switch to Azure OpenAI API.
- at the datacenter level, we bring redundacy by running our API in multiple independant regions.

## AI provider fallback

[explain more about AI provider fallback]

## Datacenter redundacy

[explain more about datacenter redundacy]