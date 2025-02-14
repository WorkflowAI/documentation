import os
import asyncio
import workflowai
from pydantic import BaseModel
from workflowai.models import Model

# Initialize WorkflowAI
workflowai.init(
    api_key=os.environ.get("WORKFLOWAI_API_KEY"),  # Make sure to set this environment variable
    base_url="https://run.workflowai.com",  # This is the default and can be omitted
)

class CityInput(BaseModel):
    city: str

class CapitalOutput(BaseModel):
    country: str
    capital: str 
    fun_fact: str

@workflowai.agent(model=Model.CLAUDE_3_5_SONNET_LATEST)
async def get_capital_info(city_input: CityInput) -> workflowai.Run[CapitalOutput]:
    """Get information about a city's country and capital."""
    return CapitalOutput(
        country="France",
        capital="Paris",
        fun_fact="Paris is known as the 'City of Light' (La Ville Lumière)"
    )

async def main():
    run = await get_capital_info(CityInput(city="Paris"))
    print(run)

if __name__ == "__main__":
    asyncio.run(main())