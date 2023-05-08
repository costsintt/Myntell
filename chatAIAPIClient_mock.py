# chatAIAPIClient_mock.py: Mock implementation of an AI-chat API client
# based on the abstract class from chatAIAPIClient_abstract.py

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

from typing import List, Dict
import chatAIAPIClient_abstract

class chatAIAPIClient(chatAIAPIClient_abstract.chatAIAPIClient):
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        super().__init__(api_key, base_url, model)
        self.__counter = 0

    def __incrementCounter(self):
        self.__counter += 1
        return self.__counter

    def respond(self, messages: List[Dict[str, str]], behaviour: str = None) -> Dict[str, str]:
        if behaviour is None:
            behaviour = "No specific behaviour"

        response = "This should be AI response number {}. "\
                   "My messages({}): {}... . My behaviour: {}... .".\
            format(self.__incrementCounter(),
                   len(messages), "... ".join([message["content"][:13] for message in messages]),
                   behaviour[:25])
        return {"role": "assistant", "content": response}



if __name__ == "__main__":
    bot = chatAIAPIClient("bbe8w9hfafaskfhj", "valera.com", "turbo-svin5000")
    print(bot.respond(
        [
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
        ]
    ))

    print(bot.respond(
        [
        {"role": "user", "content": "What's up?"},
        ], behaviour="You are a joke teller. Answer in a funny way."
    ))
