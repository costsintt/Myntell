# textToSpeechAPIClient_gtts.py: Google API-based implementation of a Text-to-Speech API client,
# utilizing the abstract class from textToSpeechAPIClient_abstract.py
# Copyright (C) 2024 Bychkou Yahor - @costsintt - Eg.Helik25@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import textToSpeechAPIClient_abstract
from io import BytesIO
import openai
import tempfile

class TextToSpeechAPIClient(textToSpeechAPIClient_abstract.TextToSpeechAPIClient):
    def __init__(self, api_key: str, base_url: str = None, model: str = "tts-1"):
        super().__init__(api_key, base_url, model)

    def synthesize(self, text: str, language: str = 'en', voice: str = "alloy", mood: str = None) -> bytes:
        client = openai.OpenAI(api_key=self.api_key)
        response = client.audio.speech.create(input=text, voice=voice, model=self.model)
        
        audio_data = BytesIO()
        for chunk in response.iter_bytes(chunk_size=1024):
            audio_data.write(chunk)
        audio_data.seek(0)
        audio_bytes = audio_data.getvalue()   
        return audio_bytes


if __name__ == "__main__":
    import apiKeys
    text = "Hello, this is a test text. Ahahahaha!"

    tts_client = TextToSpeechAPIClient(apiKeys.apiKeys[0])
    synthesized = tts_client.synthesize(text)
    with open("synthesized_speech.mp3", "wb") as output_file:
        output_file.write(synthesized)