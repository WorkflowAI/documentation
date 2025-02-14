import asyncio
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

async def main():
    # Test with a remote image of the Eiffel Tower
    print("\nTesting with remote image (Eiffel Tower)...")
    image_url = "https://images.pexels.com/photos/699466/pexels-photo-699466.jpeg"
    image = Image(url=image_url)
    run = await identify_city_from_image.run(ImageInput(image=image))
    print(run)

    # Test with a local image if available
    try:
        print("\nTesting with local image...")
        image_path = "tests/test_images/big_ben.jpg"
        with open(image_path, "rb") as image_file:
            content = base64.b64encode(image_file.read()).decode("utf-8")
        
        image = Image(content_type="image/jpeg", data=content)
        run = await identify_city_from_image.run(ImageInput(image=image))
        print(run)
    except FileNotFoundError:
        print("Local test image not found - skipping local image test")

if __name__ == "__main__":
    asyncio.run(main()) 