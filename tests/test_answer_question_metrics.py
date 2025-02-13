import asyncio
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model, Run

class Input(BaseModel):
    question: str

class Output(BaseModel):
    answer: str = Field(
        description="Answer with bullet points.",
        examples=[
            "- Answer 1",
            "- Answer 2", 
            "- Answer 3"
        ]
    )

@workflowai.agent(model=Model.CLAUDE_3_5_SONNET_LATEST)
async def answer_question(input: Input) -> Run[Output]:
    """
    Answer the question with detailed, historically accurate bullet points.
    Focus on key historical events and their significance.
    """
    ...

async def main():
    question = "What is the history of Paris?"
    print(f"\nQuestion: {question}")
    
    run = await answer_question(Input(question=question))
    print(f"Answer: {run.output.answer}")
    print(f"Cost: $ {run.cost_usd}")
    print(f"Latency: {run.duration_seconds:.2f}s")

if __name__ == "__main__":
    asyncio.run(main()) 