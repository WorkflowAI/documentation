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
    You are an expert in history.
    Answer the question with attention to detail and historical accuracy.
    """
    ...

async def main():
    question = "What is the history of Paris?"
    print(f"\nQuestion: {question}")
    run = await answer_question.run(Input(question=question))
    print(f"Answer: {run}")

    print("Completions:")
    completions = await run.fetch_completions()
    for completion in completions:
        completion_json = completion.model_dump_json(indent=2)
        print(completion_json)

    print("\nTrying with Claude 3.5 Sonnet...")
    run = await answer_question.run(Input(question=question), model=Model.CLAUDE_3_5_SONNET_LATEST)
    print(f"Answer: {run}")

    print("\nTrying with temperature=0.5...")
    run = await answer_question.run(Input(question=question), temperature=0.5)
    print(f"Answer: {run}")

    print("\nReply to the run...")
    reply_run = await run.reply(user_message="Tell me more about the 18th century.")
    print(f"Answer: {reply_run}")

if __name__ == "__main__":
    asyncio.run(main()) 