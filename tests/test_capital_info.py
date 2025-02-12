import asyncio
import workflowai
from pydantic import BaseModel
from workflowai import Model

class CityInput(BaseModel):
    city: str

class CapitalOutput(BaseModel):
    country: str
    capital: str 
    fun_fact: str

@workflowai.agent()
async def get_capital_info(city_input: CityInput) -> CapitalOutput:
    ...

async def main():
    agent_output = await get_capital_info(CityInput(city="New York"), model=Model.CLAUDE_3_5_SONNET_LATEST)
    print(f"Claude 3.5 Sonnet output:", agent_output)

    agent_output = await get_capital_info(CityInput(city="New York"), model=Model.GPT_4O_LATEST)
    print(f"GPT-4O output:", agent_output)

    agent_output = await get_capital_info(CityInput(city="New York"), model=Model.GEMINI_2_0_FLASH_LATEST)
    print(f"Gemini 2.0 Flash output:", agent_output)

if __name__ == "__main__":
    asyncio.run(main())