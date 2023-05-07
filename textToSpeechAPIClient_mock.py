# textToSpeechAPIClient_mock.py: Mock implementation of a Text-to-Speech API client
# based on the abstract class from textToSpeechAPIClient_abstract.py
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


class TextToSpeechAPIClient(textToSpeechAPIClient_abstract.TextToSpeechAPIClient):
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        super().__init__(api_key, base_url, model)

    def synthesize(self, text: str, language: str, voice: str, mood: str) -> bytes:
        #output format is mp3
        mp3Data_hexBinary = 'FF E3 18 C4 00 0C E1 0E AD B9 41 10 00 3C 0B 00 0F 70 BF F9 00 0B FF FF E0 5F C7 FF FD 08 06 06 06 2C 1F 07 C1 C0 40 31 13 82 0E FE 08 3B F4 C1 00 42 5C 1F 7F E5 1D F9 7C 87 FE 50 1F 3F 04 1C 95 FB 7F FD C6 02 11 E6 FF E3 18 C4 07 0E 2B 96 D0 01 80 50 00 8F 54 E3 CA 8C 0B 56 CA 78 FC B6 46 34 45 5F 80 E8 6A DF C4 61 E8 FD CC 6F FF FF FF FF FF FF 7F FF FF FF 98 21 0B FF FF 53 B2 82 C1 FF FF 68 C0 41 32 77 6D B6 00 7F BE 35 B1 84 FF E3 18 C4 09 0E E9 1E F2 41 C9 18 00 6A 4A B9 14 D0 A4 CA CD A1 51 12 6C 91 40 99 33 24 4D A1 50 D2 CF 21 50 99 56 48 91 93 1D 32 2A 90 54 89 A1 B3 56 F2 6A 30 08 67 12 1A 8C C4 C2 5E 54 8D 48 31 BC 01 5A 07 9F FF FF E3 18 C4 08 0C D3 32 BD 98 28 05 4A E6 FF FA 19 4B FF F9 58 C5 88 8B 00 C7 6B 28 75 8D 12 16 08 81 47 18 C6 96 52 D1 CC A3 0E 1D 12 76 FF 37 FF FF 56 33 FE EA A0 22 55 70 04 28 34 3A 86 52 D7 AF FF FA 69 59 52 9C FF E3 18 C4 0F 0A D1 62 44 00 28 10 4C D6 B5 8A 6C A2 C3 D8 B5 24 75 CF EC CA A3 01 50 F0 E4 DF FF FF FF FF FF FF F2 40 DB 95 4C 41 4D 45 33 2E 31 30 30 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55'

        return bytes.fromhex(mp3Data_hexBinary)
    

if __name__ == "__main__":
    text = "Hello, this is a test text."

    tts_client = TextToSpeechAPIClient()
    synthesized = tts_client.synthesize(text, 'en', 'valera', 'angry')
    with open("synthesized_speech.mp3", "wb") as output_file:
        output_file.write(synthesized)