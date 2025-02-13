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

@workflowai.agent(model=Model.CLAUDE_3_5_HAIKU_LATEST)
async def answer_question(input: Input) -> Output:
    """
    Answer the question with detailed, historically accurate bullet points.
    Focus on key historical events and their significance.
    """
    ...

async def main():
    question = "What is the history of Paris?"
    print(f"\nQuestion: {question}")
    async for chunk in answer_question.stream(Input(question=question), use_cache='never'):
        print(chunk)

if __name__ == "__main__":
    asyncio.run(main()) 