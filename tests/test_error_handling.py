import asyncio
from datetime import date
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model, WorkflowAIError

# Define input and output fields
class Input(BaseModel):
    transcript: str
    call_date: date

class Output(BaseModel):
    positive_points: list[str] = Field(description="List of positive points from the call", default_factory=list)
    negative_points: list[str] = Field(description="List of negative points from the call", default_factory=list)

# Define the agent
@workflowai.agent(model=Model.GEMINI_2_0_FLASH_LATEST)
async def analyze_call_feedback(input: Input) -> Output:
    """
    Analyze customer call feedback and extract positive and negative points.
    """
    ...

async def main():
    print("\nTesting error handling...")
    
    try:
        # Test with valid input
        result = await analyze_call_feedback.run(
            Input(
                transcript="[00:01:15] Customer: The product is great!",
                call_date=date(2024, 1, 15)
            )
        )
        print("Success! Result:", result)
        
    except WorkflowAIError as e:
        print("Error occurred:")
        print(f"Code: {e.code}")
        print(f"Message: {e.message}")
    
    try:
        # Test with invalid input to trigger an error
        result = await analyze_call_feedback.run(
            Input(
                transcript="",  # Empty transcript should cause an error
                call_date=date(2024, 1, 15)
            )
        )
        print("Success! Result:", result)
        
    except WorkflowAIError as e:
        print("\nExpected error occurred:")
        print(f"Code: {e.code}")
        print(f"Message: {e.message}")

if __name__ == "__main__":
    asyncio.run(main()) 