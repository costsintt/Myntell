from chatAIAPIClient_openai import ChatAIAPIClient
from speechToTextAPIClient_openai import SpeechToTextAPIClient
from textToSpeechAPIClient_openai import TextToSpeechAPIClient
from apiKeysStorage import ApiKeys

from scenario_discuss_withPredictor import Scenario


if __name__ == "__main__":
    
    from apiKeys import apiKeys
    keys = ApiKeys(apiKeys)

    sttAPI = SpeechToTextAPIClient(api_key=keys.get())
    ttsAPI = TextToSpeechAPIClient(api_key=keys.get())
    chatAPI = ChatAIAPIClient(api_key=keys.get())

    scenario = Scenario(chatAPI, keys, "Pretend you are an arrogant professor hurrying home. Your messages must be very short, one or two-sentenced.")

    import interface_user
    interface_user.sttAPI = sttAPI
    interface_user.ttsAPI = ttsAPI
    interface_user.scenario = scenario
    interface_user.keys = keys
    interface_user.start()