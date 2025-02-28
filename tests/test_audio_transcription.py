import asyncio
import os
import workflowai
from pydantic import BaseModel, Field
from workflowai.fields import Audio

class AudioInput(BaseModel):
    audio: Audio = Field(description="The audio file to transcribe")

class AudioOutput(BaseModel):
    transcription: str = Field(description="The transcription of the audio content")

@workflowai.agent(id="audio-transcription")
async def audio_transcription(input: AudioInput) -> AudioOutput:
    """
    Transcribe the audio file accurately.
    Capture all spoken words and maintain proper punctuation.
    """
    ...

async def main():
    print("\nChecking model compatibility for audio transcription...")
    models = await audio_transcription.list_models()
    
    supported_models = []
    unsupported_models = []
    
    for model in models:
        if model.is_not_supported_reason is None:
            supported_models.append(model.id)
            print(f"✅ {model.id} supports audio transcription")
        else:
            unsupported_models.append((model.id, model.is_not_supported_reason))
            print(f"❌ {model.id} does not support audio transcription: {model.is_not_supported_reason}")
    
    # Assert that we have at least one supported model and one unsupported model
    assert len(supported_models) > 0, "No models support audio transcription"
    assert len(unsupported_models) > 0, "All models support audio transcription (unexpected)"
    
    print(f"\nFound {len(supported_models)} models that support audio transcription")
    print(f"Found {len(unsupported_models)} models that do not support audio transcription")
    
    # If you want to test with an actual audio file, uncomment the following code:
    """
    # Example with a remote audio file
    audio_url = "https://example.com/sample-audio.mp3"
    audio = Audio(url=audio_url)
    
    # Run with a compatible model (first one from the supported list)
    if supported_models:
        compatible_model = supported_models[0]
        print(f"\nRunning transcription with {compatible_model}...")
        run = await audio_transcription.run(
            AudioInput(audio=audio),
            model=compatible_model
        )
        print(f"Transcription: {run.transcription}")
    """

if __name__ == "__main__":
    asyncio.run(main()) 