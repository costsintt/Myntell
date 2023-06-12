# f'Check the transcribed audio input for speech errors, including\
#   incorrect sentence formation, missing or incorrect prepositions, and any\
#   other speech and logical errors. If the sentence is correct, output "Correct."\
#   If the sentence is incorrect, provide an explanation\
#   for each problem found. The message: "{message}".'

import sounddevice as sd
import soundfile as sf
import numpy as np

from io import BytesIO
from typing import Union, BinaryIO

import pygame

from chatAIAPIClient_openai import ChatAIAPIClient
from speechToTextAPIClient_openai import SpeechToTextAPIClient
from textToSpeechAPIClient_gtts import TextToSpeechAPIClient
from chatbot import Chatbot


class AudioRecorder:
    def __init__(self, samplerate=44100):
        self.isRecording = False
        self.samplerate = samplerate
        self.buffer = []
        self.stream = sd.InputStream(callback=self.callback, channels=1, samplerate=samplerate)

    def callback(self, indata, frames, time, status):
        self.buffer.append(indata.copy())

    def start_recording(self):
        if not self.isRecording:
            self.isRecording = True
            self.stream.start()

    def stop_recording(self):
        if self.isRecording:
            self.isRecording = False
            self.stream.stop()
            recording = np.concatenate(self.buffer, axis=0)
            self.buffer = []
            return recording

def file_read(filename: str) -> Union[BytesIO, None]:
    try:
        with open(filename, 'rb') as file:
            content = file.read()
    except FileNotFoundError:
        return None
    else:
        clone = BytesIO(content)
        return clone

def file_write(fileToWrite: BytesIO, filename: str) -> None:
    with open(filename, 'wb') as file:
        file.write(fileToWrite.getbuffer())

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    from apiKeys import apiKey_openai

    sttAPI = SpeechToTextAPIClient(api_key=apiKey_openai)
    ttsAPI = TextToSpeechAPIClient()
    chatAPI = ChatAIAPIClient(api_key=apiKey_openai)
    
    grammarBot = Chatbot(chatAPI,
                         behaviour="Correct grammar and assist non-English speakers in expressing \
                            themselves in English. If the input text is not in English, translate \
                            it into English.")
    conversationalBot = Chatbot(chatAPI)

    recorder = AudioRecorder()

    isRecording = False
    while(True):
        command = input()
        if command == '1':
            print("Recording started...", sep='')
            isRecording = True
            recorder.start_recording()
        elif (command == '2' or command == '3') and isRecording:
            print("STOPPED")
            isRecording = False
            data = recorder.stop_recording()
            audioFile = BytesIO()
            sf.write(audioFile, data, 44100, format="wav")
            audioFile.seek(0)
            
            print("---GRAMMAR---") if command == '2' else print("---CONVERSATION---")
            userMessage = sttAPI.transcribe(audioFile)
            print("User:\t", userMessage)
            botMessage = grammarBot.chat(userMessage) if command == '2' else conversationalBot.chat(userMessage)
            print("Bot:\t", botMessage)
            
            audioFile.seek(0)
            audioFile.truncate(0)
            audioFile.write(ttsAPI.synthesize(botMessage))

            audioFile.seek(0)
            file_write(audioFile, "temp.mp3")
            pygame.mixer.music.load("temp.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        elif command == '4' or command == '5':
            print("---GRAMMAR---") if command == '4' else print("---CONVERSATION---")
            userMessage = input('write input: ')
            botMessage = grammarBot.chat(userMessage) if command == '4' else conversationalBot.chat(userMessage)
            print("Bot:\t", botMessage)


        elif command == '0':
            print("ALL MESSAGES")
            print("---conversational bot---")
            for message in conversationalBot.messages:
                print(message)
            print("---grammar bot---")
            for message in conversationalBot.messages:
                print(message)