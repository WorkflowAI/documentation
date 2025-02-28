import asyncio
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

async def main():
    # Sample transcript for testing
    sample_transcript = """
    [00:01:23] Customer: I really love how easy the app is to use. The interface is so intuitive.
    [00:02:45] Customer: However, I've been having issues with the loading times. Sometimes it takes forever to load.
    [00:03:30] Customer: But the customer service has been excellent, they always respond quickly.
    """
    
    input_data = CallFeedbackInput(
        transcript=sample_transcript,
        call_date='2025-01-01'
    )
    
    run = await analyze_call_feedback(input_data)
    print(run)

if __name__ == "__main__":
    asyncio.run(main()) 