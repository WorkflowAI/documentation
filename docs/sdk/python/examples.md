# Examples

## Analyze a customer feedback call transcript

For example, the following agent analyzes a customer feedback call transcript, with:
- as input: a transcript and a date
- as output: a list of positive and negative feedback points, each with a supporting quote and timestamp

```python
import workflowai
from pydantic import BaseModel, Field
from typing import List
from datetime import date
from workflowai import Model

# The input class defines all the information the AI agent needs that is not part of the instructions
class CallFeedbackInput(BaseModel):
    """Input for analyzing a customer feedback call."""
    transcript: str = Field(description="The full transcript of the customer feedback call.")
    call_date: date = Field(description="The date when the call took place.")

# Model representing a single feedback point with supporting evidence
class FeedbackPoint(BaseModel):
    """A specific feedback point with its supporting quote."""
    point: str = Field(description="The main point or insight from the feedback.")
    quote: str = Field(description="The exact quote from the transcript supporting this point.")
    timestamp: str = Field(description="The timestamp or context of when this was mentioned in the call.")

# Model representing the structured analysis of the customer feedback call
class CallFeedbackOutput(BaseModel):
    """Structured analysis of the customer feedback call."""
    positive_points: List[FeedbackPoint] = Field(
        default_factory=list,
        description="List of positive feedback points, each with a supporting quote."
    )
    negative_points: List[FeedbackPoint] = Field(
        default_factory=list,
        description="List of negative feedback points, each with a supporting quote."
    )

@workflowai.agent(id="analyze-call-feedback", model=Model.GPT_4O_LATEST)
async def analyze_call_feedback(input: CallFeedbackInput) -> CallFeedbackOutput:
    """
    Analyze a customer feedback call transcript to extract key insights:
    1. Identify positive feedback points with supporting quotes
    2. Identify negative feedback points with supporting quotes
    3. Include timestamp/context for each point

    Be specific and objective in the analysis. Use exact quotes from the transcript.
    Maintain the customer's original wording in quotes.
    """
    ...

run = await analyze_call_feedback(CallFeedbackInput(transcript="...", call_date='2025-01-01'))
print(run)
```
