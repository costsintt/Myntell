# textToSpeechAPIClient_abstract.py: Abstract class for a Text-to-Speech API client implementation
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

from abc import ABC, abstractmethod

class TextToSpeechAPIClient(ABC):
    def __init__(self, api_key: str, base_url: str = None, model: str = None):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model

    @abstractmethod
    def synthesize(self, text: str, language: str = None, voice: str = None, mood: str = None) -> bytes:
        #output format is mp3
        pass