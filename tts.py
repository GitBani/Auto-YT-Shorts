# from gtts import gTTS
from openai import OpenAI
from pydub import AudioSegment
from random import randrange


def _speedup_mp3(mp3_file_name: str, speed: float) -> None:
    audio = AudioSegment.from_file(mp3_file_name, format="mp3")
    faster_audio = audio.speedup(playback_speed = speed)
    faster_audio.export(mp3_file_name, format="mp3") 


def tts_rand_voice(text: str, mp3_file_name: str) -> None:
    client = OpenAI()
    voices = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
    selected_voice_idx = randrange(0, len(voices))
    response = client.audio.speech.create(
        model = 'tts-1',
        voice = voices[selected_voice_idx],
        input = text
    )
    response.stream_to_file(mp3_file_name)
    _speedup_mp3(mp3_file_name, 1.25)
