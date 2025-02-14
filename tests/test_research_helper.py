import asyncio
import httpx
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Annotated
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model

# Define the tools
def get_current_time(timezone: Annotated[str, "The timezone to get the current time in. e-g Europe/Paris"]) -> str:
    """Return the current time in the given timezone in iso format"""
    return datetime.now(ZoneInfo(timezone)).isoformat()

async def get_latest_pip_version(package_name: Annotated[str, "The name of the pip package to check"]) -> str:
    """Fetch the latest version of a pip package from PyPI"""
    url = f"https://pypi.org/pypi/{package_name}/json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return data['info']['version']

class Input(BaseModel):
    question: str = Field(description="The research question to answer")

class Output(BaseModel):
    answer: str = Field(description="The researched answer with relevant information")

@workflowai.agent(
    id="research-helper",
    tools=[get_current_time, get_latest_pip_version],
    model=Model.GPT_4O_LATEST
)
async def research_question(input: Input) -> Output:
    """
    Research helper that can:
    1. Get current time in different timezones
    2. Check latest versions of Python packages on PyPI
    """
    ...

async def main():
    # Test time-related question
    print("\nTesting time-related question...")
    run = await research_question.run(
        Input(question="What is the current time in Phoenix, AZ?")
    )
    print(run)

    # Test package version question
    print("\nTesting package version question...")
    run = await research_question.run(
        Input(question="What is the latest version of workflowai package?")
    )
    print(run)

if __name__ == "__main__":
    asyncio.run(main()) 