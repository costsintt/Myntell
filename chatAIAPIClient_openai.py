# chatAIAPIClient_openai.py: OpenAI API-based implementation of an AI-chat API client,
# utilizing the abstract class from chatAIAPIClient_abstract.py

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

from typing import Dict, List
import openai
import chatAIAPIClient_abstract

class chatAIAPIClient(chatAIAPIClient_abstract.chatAIAPIClient):
    def __init__(self, api_key: str, base_url: str = None, model: str = "gpt-3.5-turbo"):
        super().__init__(api_key, base_url, model)

    def respond(self, messages: List[Dict[str, str]], behaviour: str = None):
        openai.api_key = self.api_key
        firstMessage = {"role": "user", "content": behaviour}
        messages.insert(0, firstMessage)
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        return response.choices[0].message['content']
    

if __name__ == "__main__":
    import apiKeys
    bot = chatAIAPIClient(api_key=apiKeys.apiKey_openai)

    print(bot.respond(
        [
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
        ], behaviour="You are a helpful assistant."
    ))

    print(bot.respond(
        [
        {"role": "user", "content": "What's up?"},
        ], behaviour="You are a joke teller. Answer in a funny way."
    ))