import os
import asyncio
import workflowai
from pydantic import BaseModel, Field
from workflowai.fields import Audio

class AudioInput(BaseModel):
    audio: Audio = Field(description="The audio file to transcribe")

class AudioOutput(BaseModel):
    transcription: str = Field(description="The transcribed text from the audio")

@workflowai.agent(id="audio-transcription")
async def audio_transcription(input: AudioInput) -> AudioOutput:
    """
    Transcribe the audio file.
    """
    ...

async def test_model_compatibility():
    # Get list of models
    models = await audio_transcription.list_models()
    
    for model in models:
        if model.is_not_supported_reason is None:
            print(f"{model.id} supports audio transcription")
        else:
            print(f"{model.id} does not support audio transcription: {model.is_not_supported_reason}")

if __name__ == "__main__":
    asyncio.run(test_model_compatibility()) 