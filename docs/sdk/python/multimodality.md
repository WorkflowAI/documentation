# Multimodality

Build agents that can handle multiple modalities, such as images, PDF, documents, audio, and video.

## Images

Add images as input to an agent by using the `Image` class. An image can either have:

- a `content`, base64 encoded data
- a `url`

In the following example, we'll build an agent that can identify the city and country from an image.

```python
import base64
import workflowai
from workflowai import Model
from workflowai.fields import Image
from pydantic import BaseModel, Field
from typing import Optional

class ImageInput(BaseModel):
    image: Image = Field(description="The image to analyze")

class ImageOutput(BaseModel):
    city: str = Field(default="", description="Name of the city shown in the image")
    country: str = Field(default="", description="Name of the country where the city is located")
    confidence: Optional[float] = Field(
        default=None,
        description="Confidence level in the identification (0-1)",
    )

@workflowai.agent(id="city-identifier", model=Model.GEMINI_2_0_FLASH_LATEST)
async def identify_city_from_image(image_input: ImageInput) -> ImageOutput:
    """
    Analyze the provided image and identify the city and country shown in it.
    If the image shows a recognizable landmark or cityscape, identify the city and country.
    If uncertain, indicate lower confidence or leave fields empty.

    Focus on:
    - Famous landmarks
    - Distinctive architecture
    - Recognizable skylines
    - Cultural elements that identify the location

    Return empty strings if the city/country cannot be determined with reasonable confidence.
    """
    ...

# Run the agent

## From a remote image
image_url = "https://images.pexels.com/photos/699466/pexels-photo-699466.jpeg"
image = Image(url=image_url)
agent_run = await identify_city_from_image.run(ImageInput(image=image))
print(agent_run)

# Output:
# ==================================================
# {
#   "city": "Paris",
#   "country": "France",
#   "confidence": 1.0
# }
# ==================================================
# Cost: $ 0.00024
# Latency: 6.70s

## From a local image
image_path = "path/to/image.jpg"
with open(image_path, "rb") as image_file:
    content = base64.b64encode(image_file.read()).decode("utf-8")

image = Image(content_type="image/jpeg", data=content)
agent_run = await identify_city_from_image.run(ImageInput(image=image))
```

See a more complete example in [examples/07_image_agent.py](https://github.com/WorkflowAI/workflowai-py/blob/main/examples/07_image_agent.py).

{% hint style="info" %}
You can test this agent with your own images in the WorkflowAI playground. View on [WorkflowAI](https://workflowai.com/docs/agents/city-identifier/1).
{% endhint %}

![Compare models](/docs/assets/images/agents/city-identifier/playground.png)

{% hint style="info" %}
Images generation is not supported yet.
{% endhint %}

## PDF, documents

Use the `File` class to add PDF, documents, or other files as input to an agent.

In the following example, we'll build an agent that can answer questions based on a PDF document.

```python
import workflowai
from pydantic import BaseModel, Field
from workflowai import Model
from workflowai.fields import File

class PDFQuestionInput(BaseModel):
    pdf: File = Field(description="The PDF document to analyze")
    question: str = Field(description="The question to answer about the PDF content")

class PDFAnswerOutput(BaseModel):
    answer: str = Field(description="The answer to the question based on the PDF content")
    quotes: list[str] = Field(description="Relevant quotes from the PDF that support the answer")

@workflowai.agent(id="pdf-answer-bot", model=Model.CLAUDE_3_5_SONNET_LATEST)
async def answer_pdf_question(input: PDFQuestionInput) -> PDFAnswerOutput:
    """
    Analyze the provided PDF document and answer the given question.
    Provide a clear and concise answer based on the content found in the PDF.
    Include relevant quotes to support the answer.
    """
    ...

# Run the agent

## From a remote file
pdf_url = "https://microsoft.gcs-web.com/static-files/b3eef820-6757-44ea-9f98-3963bace4837"
pdf = File(url=pdf_url)
agent_run = await answer_pdf_question.run(
    PDFQuestionInput(
        pdf=pdf,
        question="What are the main takeaways from the document?"
    )
)
print(agent_run)

# Output:
# ==================================================
# ...

## From a local file

pdf_path = "path/to/pdf.pdf"
with open(pdf_path, "rb") as pdf_file:
    content = pdf_file.read()

pdf = File(content_type="application/pdf", data=content)
agent_run = await answer_pdf_question.run(
    PDFQuestionInput(
        pdf=pdf,
        question="What are the main takeaways from the document?"
    )
)
```

{% hint style="info" %}
Try this `pdf-answer-bot` with [your own PDF in the WorkflowAI playground](https://workflowai.com/docs/agents/pdf-answer-bot/1).
{% endhint %}

## Audio

## Video
