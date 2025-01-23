# Evaluating your AI agent

{% hint style="info" %}
Accessible for product managers, and engineers.
{% endhint %}

![Benchmarks](</docs/assets/images/benchmarks.png>)

When you are building a AI agent, you will often want to compare the performance, cost and latency of different [versions](/docs/concepts/versions.md) of your agent. For example, imagine you are building an agent that translate text into a different language, and you want to compare accuracy of the translation, cost and latency between GPT-4o, GPT-4o-mini, Gemini 1.5 Flash and LLAMA 3.1 (8B).

In this section, we will learn:
- what metrics are compared in benchmarks
- how to leave a first positive or negative review
- how AI reviews are generated
- how to run benchmarks to compare different versions of your agent
- how to adjust how AI reviews are generated

## Metrics

### Positive and negative reviews

We define a review as the evaluation (positive or negative) given to a specific output of an agent. For example, if you are building a agent that write description of images, a review will be the evaluation given to specific description of an image for a specific agent that generated this description.

WorkflowAI currently only supports **positive** reviews, or **negative** reviews (binary outcome).

### Cost

**Cost** represents how much (in $) you pay for the agent to perform a task. This is an objective metric that is automatically computed by WorkflowAI.

### Latency

**Latency** measures how long (in seconds) it takes for the agent to perform a task. Like cost, this is an objective metric that is automatically computed by WorkflowAI.

## How to leave a first review

From the playground, run your agent and look at the outputs section. Then leave a review by clicking on the thumbs up or thumbs down icon.

![Leave a review](/docs/assets/images/benchmarks/leave-review.png)


Once you leave a review, WorkflowAI will use AI to generate reviews for the other remaining outputs.

## How AI reviews are generated

AI-generated reviews are a feature of WorkflowAI that uses an AI agent to review the outputs of other versions automatically. 

For example, let's say you're building an agent that summarizes articles. After you leave your first review on one summary, WorkflowAI will automatically use AI to evaluate and generate reviews for all other summaries produced by different versions of your agent.

![AI-generated reviews](</docs/assets/images/playground-reviews.png>)

## Running benchmarks



## Adjusting AI reviews