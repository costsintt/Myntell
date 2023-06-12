# speechToTextAPIClient_openai.py: OpenAI API-based implementation of a Speech-to-Text API client,
# utilizing the abstract class from speechToTextAPIClient_abstract.py
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

from io import BytesIO
from typing import BinaryIO, Union
import openai
import speechToTextAPIClient_abstract

class SpeechToTextAPIClient(speechToTextAPIClient_abstract.SpeechToTextAPIClient):
    def __init__(self, api_key: str, base_url: str = None, model: str = "whisper-1"):
        super().__init__(api_key, base_url, model)

    def transcribe(self, audioStream: Union[BytesIO, BinaryIO], format: str = 'wav', language: str = 'en-US') -> str:
        audioStream.name = "temp." + format
        transcript = openai.Audio.transcribe(model=self.model, file=audioStream,
                                             api_key=self.api_key)
        return transcript.text