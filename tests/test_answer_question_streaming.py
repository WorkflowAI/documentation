import asyncio
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model
from collections.abc import AsyncIterator

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
def answer_question_stream(input: Input) -> AsyncIterator[Output]:
    """
    Answer the question with detailed, historically accurate bullet points.
    Focus on key historical events and their significance.
    """
    ...

async def main():
    question = "What is the history of Paris?"
    print(f"\nQuestion: {question}")
    async for chunk in answer_question_stream(Input(question=question)):
        print(chunk.answer)

if __name__ == "__main__":
    asyncio.run(main()) 