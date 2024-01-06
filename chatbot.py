# chatbot.py: Class for chatting with an AI, utilizing the abstract class from chatAIAPIClient_abstract.py
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

from chatAIAPIClient_abstract import ChatAIAPIClient

from typing import List, Dict

class Chatbot:
    def __init__(self, APIClient: ChatAIAPIClient, behaviour: str = None,
                 numberOfActiveMessages : int = 5):
        self.APIClient = APIClient
        
        self.messages = []
        self.numberOfActiveMessages = numberOfActiveMessages

        if behaviour is not None:
            self.behaviour = behaviour
        else:
          self.behaviour = "Improvise entertaining and not long responses,"\
                           "even if you lack knowledge on a subject."

    def chat(self, message: str):
        self.messages.append({"role": "user", "content": message})

        response = self.APIClient.respond(messages=list(self.messages[-self.numberOfActiveMessages:]),
                                          behaviour=self.behaviour)

        self.messages.append(response)
        
        return response['content']
    
    def chat_withoutMemory(self, messages: List[Dict[str, str]], numberOfActoveMessages: int):
        response = self.APIClient.respond(messages=list(messages[-numberOfActoveMessages:]),
                                          behaviour=self.behaviour)
        return response


if __name__ == "__main__":
    from apiKeys import apiKey_openai
    from chatAIAPIClient_mock import ChatAIAPIClient

    api = ChatAIAPIClient(api_key=apiKey_openai)
    
    bot = Chatbot(api, numberOfActiveMessages=5)

    print(bot.chat("M1"))
    print(bot.chat("M2"))
    print(bot.chat("M3"))
    print(bot.chat("M4"))
    print(bot.chat("M5"))
    print(bot.chat("M6"))