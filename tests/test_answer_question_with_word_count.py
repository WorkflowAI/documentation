import asyncio
import workflowai
from pydantic import BaseModel
from workflowai import Model

class Input(BaseModel):
    question: str
    word_count: int

class Output(BaseModel):
    answer: str

@workflowai.agent(
    id="answer-question-with-word-count",
    model=Model.CLAUDE_3_5_HAIKU_LATEST
)
async def answer_question(input: Input) -> Output:
    """
    The answer should be less than {{ word_count }} words.
    Answer the following question:
    {{ question }}
    """
    ...

async def main():
    # Test with a short word count
    print("\nTesting with 5-word limit...")
    run = await answer_question.run(
        Input(
            question="What is artificial intelligence?",
            word_count=5
        )
    )
    print(run)
    
    # Test with a longer word count
    print("\nTesting with 20-word limit...")
    run = await answer_question.run(
        Input(
            question="Explain how neural networks work",
            word_count=20
        )
    )
    print(run)

if __name__ == "__main__":
    asyncio.run(main()) 