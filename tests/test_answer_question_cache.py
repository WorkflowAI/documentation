import asyncio
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model, Run
from workflowai.core.domain.cache_usage import CacheUsage

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

# Use cache at agent level
@workflowai.agent(model=Model.CLAUDE_3_5_SONNET_LATEST)
async def answer_question(input: Input) -> Output:
    """
    Answer the question with detailed, historically accurate bullet points.
    Focus on key historical events and their significance.
    """
    ...

async def main():
    question = "What is the history of Paris?"
    print(f"\nQuestion: {question}")
    
    # Default behavior (use cache if available)
    print("\nDefault run (use cache if available):")
    run = await answer_question.run(Input(question=question))
    print(run)
    
    # Always use cache if available
    print("\nAlways cache run:")
    cached_run = await answer_question.run(Input(question=question), use_cache='always')
    print(cached_run)
    
    # Never use cache
    print("\nNever use cache run:")
    no_cache_run = await answer_question.run(Input(question=question), use_cache='never')
    print(no_cache_run)
    
    # Prefer using cache but allow fallback to API
    print("\nPrefer cache run:")
    prefer_cache_run = await answer_question.run(Input(question=question), use_cache='auto')
    print(prefer_cache_run)

if __name__ == "__main__":
    asyncio.run(main()) 