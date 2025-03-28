import asyncio
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model
from workflowai.fields import PDF

class PDFQuestionInput(BaseModel):
    pdf: PDF = Field(description="The PDF document to analyze")
    question: str = Field(description="The question to answer about the PDF content")

class PDFAnswerOutput(BaseModel):
    answer: str = Field(description="The answer to the question based on the PDF content")
    quotes: list[str] = Field(description="Relevant quotes from the PDF that support the answer")

@workflowai.agent(id="pdf-answer-bot", model=Model.GEMINI_2_0_FLASH_LATEST)
async def answer_pdf_question(input: PDFQuestionInput) -> PDFAnswerOutput:
    """
    Analyze the provided PDF document and answer the given question.
    Provide a clear and concise answer based on the content found in the PDF.
    Include relevant quotes to support the answer.
    """
    ...

async def main():
    # Test with a remote PDF (Microsoft's annual report)
    print("\nTesting with remote PDF...")
    pdf_url = "https://microsoft.gcs-web.com/static-files/b3eef820-6757-44ea-9f98-3963bace4837"
    pdf = PDF(url=pdf_url)
    run = await answer_pdf_question.run(
        PDFQuestionInput(
            pdf=pdf,
            question="What are the main points from the PDF?"
        )
    )
    print(run)

if __name__ == "__main__":
    asyncio.run(main()) 