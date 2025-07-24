# Text-to-Speech (TTS) Demo

This is a simple demo using the open-source ([Kokoro TTS model](https://huggingface.co/hexgrad/Kokoro-82M)) to convert text into speech.

## What It Does
- Converts your input text to speech using the Kokoro TTS model  
- Saves output as `.wav` files in the `Output_audio/` folder  
- Automatically removes old audio files before generating new ones  
- Plays the generated audio files for you  

## How to Use
1. Run the script  
2. Enter the text you want to convert  
3. The script will:
   - Delete any existing `.wav` files in `Output_audio/`
   - Generate new audio files (`0.wav`, `1.wav`, etc.)
   - Play the new audio files automatically  