## Runs
A run is a single execution of an agent. By default, WorkflowAI stores all runs, available in the "Runs" section.

![alt text](<Screenshot 2025-01-03 at 17.04.12.png>)

### Why storing all runs?
- **Observability**: Understand how the AI is performing by tracking and analyzing its outputs over time.
- **Saving cost**: For the same input and model versions, cached runs can be served without triggering a new LLM call, reducing costs to $0 for serving cached runs.
- **Fine-Tuning and distillation**: Saving all runs is required for fine-tuning models and distillation processes.

### How to search runs?
WorkflowAI provides a powerful search – available under the "Runs" section – to find specific runs:

![alt text](<Screenshot 2025-01-03 at 17.11.48.png>)

> Architecture: under the hood, runs are stored in a Clickhouse database, which is optimized for handling large amount of data, and for fast search and aggregation queries. Clickhouse also compresses data, which reduces storage costs. Learn more about Clickhouse [here](https://clickhouse.com/docs/en/introduction).

### View a run

### View a run prompt

### Try in playground