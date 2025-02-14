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

## Audio

## Video

