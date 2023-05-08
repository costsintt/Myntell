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

from collections import deque
from chatAIAPIClient_abstract import chatAIAPIClient

class Chatbot:
    def __init__(self, APIClient: chatAIAPIClient, behaviour: str = None):
        self.APIClient = APIClient
        
        messages = []
        self.messages = deque(messages, maxlen=5)

        if behaviour is not None:
            self.behaviour = behaviour
        else:
          self.behaviour = "Be a humorous companion and improvise entertaining responses,"\
                           "even if you lack knowledge on a subject."

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})

        response = self.APIClient.respond(messages=list(self.messages), behaviour=self.behaviour)

        self.messages.append(response)
        
        return response['content']


if __name__ == "__main__":
    from apiKeys import apiKey_openai
    from chatAIAPIClient_mock import chatAIAPIClient

    api = chatAIAPIClient(api_key=apiKey_openai)
    
    bot = Chatbot(api)

    print(bot.chat("What's your name?"))
    print(bot.chat("What?"))