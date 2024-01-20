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

from abc import ABC, abstractmethod

from chatAIAPIClient_abstract import ChatAIAPIClient
from apiKeysStorage import ApiKeys

class Scenario(ABC):
    def __init__(self, chatAPI: ChatAIAPIClient, keys: ApiKeys):
        self.chatAPI = chatAPI
        self.keys = keys

    @abstractmethod
    def answer(self, newUserMessage: str) -> str:
        pass

    @abstractmethod
    def getAdditionalInfo(self) -> str:
        pass