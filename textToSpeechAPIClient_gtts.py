# textToSpeechAPIClient_gtts.py: Google API-based implementation of a Text-to-Speech API client,
# utilizing the abstract class from textToSpeechAPIClient_abstract.py
# Copyright (C) 2023 Bychkou Yahor - @costsintt - Eg.Helik25@gmail.com

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
from gtts import gTTS
from io import BytesIO

class TextToSpeechAPIClient(textToSpeechAPIClient_abstract.TextToSpeechAPIClient):
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        super().__init__(api_key, base_url, model)

    def synthesize(self, text: str, language: str = None, voice: str = None, mood: str = None) -> bytes:
        tts = gTTS(text=text)
        
        with BytesIO() as audioData:
            tts.write_to_fp(audioData)
            audio_bytes = audioData.getvalue()

        return audio_bytes


if __name__ == "__main__":
    text = "Hello, this is a test text. Ahahahaha!"

    tts_client = TextToSpeechAPIClient()
    synthesized = tts_client.synthesize(text)
    with open("synthesized_speech.mp3", "wb") as output_file:
        output_file.write(synthesized)