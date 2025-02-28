import asyncio
import workflowai
from pydantic import BaseModel, Field
from enum import Enum
from typing import List
from workflowai import Model

class ChatbotInput(BaseModel):
    user_message: str

class Recommendation(BaseModel):
    name: str
    address: str

class ChatbotOutput(BaseModel):
    assistant_message: str
    recommendations: list[Recommendation]

@workflowai.agent(id="travel-assistant", model=Model.GPT_4O_LATEST)
async def chat(input: ChatbotInput) -> ChatbotOutput:
    """
    A helpful travel assistant that can provide recommendations and answer questions about destinations.
    """
    ...

async def main():
    print("\nStarting conversation with travel assistant...")
    
    # Initial question about travel
    run = await chat.run(ChatbotInput(user_message="I'm planning a trip to Paris. What are the must-see attractions?"))
    print(run)

    # Follow-up about best time to visit
    run = await run.reply(user_message="When is the best time of year to visit?")
    print(run)

    # Ask about local cuisine
    run = await run.reply(user_message="What local dishes should I try?")
    print(run)

    print(f"\nConversation cost: ${run.cost_usd}")
    print(f"Total duration: {run.duration_seconds:.2f}s")

if __name__ == "__main__":
    asyncio.run(main()) 