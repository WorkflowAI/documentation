import asyncio
import workflowai
from typing import Literal
from pydantic import BaseModel, Field
from workflowai import Model
import os

class Input(BaseModel):
    question: str

class Output(BaseModel):
    category: Literal["billing", "technical", "account", "other"]

@workflowai.agent(id="triage-agent", model=Model.CLAUDE_3_5_HAIKU_LATEST)
async def triage_question(input: Input) -> Output:
    """
    Triage a customer question into different categories.
    """
    ...

@workflowai.agent(
    id="triage-agent",
    model=Model.CLAUDE_3_5_HAIKU_LATEST
)
async def triage_question_2(input: Input) -> Output:
    """
    Triage a customer question into different categories.

    Categories:
    - billing: Questions about payments, invoices, pricing, or subscription changes
    - technical: Questions about API usage, SDK implementation, or technical issues
    - account: Questions about account access, settings, or profile management
    - other: Questions that don't fit into the above categories
    """
    ...

async def main():
    print(os.environ.get("WORKFLOWAI_API_KEY"))

    run = await triage_question.run(Input(question="How do I change my billing information?"))
    print(run)

    run = await triage_question_2.run(Input(question="How do I change my billing information?"))
    print(run)

if __name__ == "__main__":
    asyncio.run(main()) 