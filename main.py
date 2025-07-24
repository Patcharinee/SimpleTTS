from kokoro import KPipeline
import soundfile as sf
import torch
from playsound import playsound
import os

# Define parameters
voice = 'af_heart'
output_dir = 'Output_audio'

# Input text from user
text = input('Enter the text to convert to audio: ')
#text = f'''Good morning ! How are you doing today?'''

def text_to_audio_files(text, voice=voice, output_dir=output_dir):
    """
    Convert input text to audio files using Kokoro TTS pipeline.
    Args:
        text (str): The input text to convert to audio.
        voice (str): The voice to use for synthesis.
        output_dir (str): Directory to save output audio files.
    Returns:
        List[str]: List of output audio file paths.
    """
    os.makedirs(output_dir, exist_ok=True)
    # Delete all existing .wav files in the output directory
    for filename in os.listdir(output_dir):
        if filename.endswith('.wav'):
            file_path = os.path.join(output_dir, filename)
            try:
                os.remove(file_path)
                print(f'Deleted {file_path}')
            except Exception as e:
                print(f'Could not delete {file_path}: {e}')
    pipeline = KPipeline(lang_code='a')
    generator = pipeline(text, voice=voice)
    audio_files = []
    for i, (gs, ps, audio) in enumerate(generator):
        print(i, gs, ps)
        audio_path = f'{output_dir}/{i}.wav'
        sf.write(audio_path, audio, 24000)
        audio_files.append(audio_path)
    return audio_files

audio_files = text_to_audio_files(text, voice, output_dir)
for audio_file in audio_files:
    playsound(audio_file)

