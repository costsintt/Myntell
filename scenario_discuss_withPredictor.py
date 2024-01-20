# chatAIAPIClient_abstract.py: Abstract class for an AI-chat API client implementation
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

import scenario_abstract

from chatAIAPIClient_abstract import ChatAIAPIClient
from apiKeysStorage import ApiKeys
from chatbot import Chatbot

def convert_dicts_to_string(dicts_list):
    result_string = ""
    for dict_item in dicts_list:
        name = dict_item['role']
        if name == "user": name = "First person"
        elif name == "assistant": name = "Second person"
        else: name = "Someone"
        content = dict_item['content']
        result_string += f"{name}: {content}\n\n"
    return result_string

class Scenario(scenario_abstract.Scenario):
    def __init__(self, chatAPI: ChatAIAPIClient, keys: ApiKeys, theme: str):
        super().__init__(chatAPI=chatAPI, keys=keys)

        self.theme = theme
        self.conversationalBot = Chatbot(self.chatAPI, numberOfActiveMessages=14, behaviour=self.theme)
        self.predictorBot = Chatbot(self.chatAPI, behaviour="You are given a transcript of a conversation. Your task is to predict and generate a response that might match the next message in the conversation, considering the context, tone, and content.")


    def answer(self, newUserMessage: str) -> str:
        self.chatAPI.api_key = self.keys.get()
        answer = self.conversationalBot.chat(newUserMessage)

        discussionToPredict = convert_dicts_to_string(self.conversationalBot.getLastActiveMessages())
        prediction = self.predictorBot.chat_withoutMemory(discussionToPredict)['content']
        self.additionalInfo = f"\nPredictor said:---\n{prediction}\n---"

        return answer


    def getAdditionalInfo(self) -> str:
        return self.additionalInfo

