import asyncio
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model

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

@workflowai.agent(model=Model.GPT_4O_LATEST)
async def answer_question(input: Input) -> Output:
    """
    Answer the question with detailed, historically accurate bullet points.
    Focus on key historical events and their significance.
    """
    ...

async def main():
    question = "What is the history of Paris?"
    print(f"\nQuestion: {question}")
    run = await answer_question(Input(question=question))
    print(f"Answer: {run}")

    print("\nTrying with Claude 3.5 Sonnet...")
    run = await answer_question(Input(question=question), model=Model.CLAUDE_3_5_SONNET_LATEST)
    print(f"Answer: {run}")

if __name__ == "__main__":
    asyncio.run(main()) 