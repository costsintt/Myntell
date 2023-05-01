from speechTools import *
from info import *

import sounddevice as sd
import soundfile as sf

import time
import keyboard
import numpy as np
import math
import boto3
import requests
import openai
import chatbot
import os
import shutil


if __name__ == "__main__":
    
    listForSavingConversationInText = []

    fileName_synthesized = 'output.mp3'
    fileName_micRecorded = 'outoutMicFile.mp3'
    fileName_micRecordedToText = 'micOutPut.txt'

    recordedAudioFromMic = None
    sampleRate = 44100
    numOfChannels = 2
    maxDuration = 30
    isMicRecording = False

    timeOfStartedAudioRecordingFromMic = 0.0

    botik = chatbot.Chatbot()

    while(True):
        if not isMicRecording and keyboard.is_pressed('shift+alt+1'):
            print("[Mic recording: STARTED]")
            isMicRecording = True
            timeOfStartedAudioRecordingFromMic = time.time()
            recordedAudioFromMic = sd.rec(int(sampleRate * maxDuration),
                                          samplerate = sampleRate, channels = numOfChannels)
            
        if isMicRecording and keyboard.is_pressed('shift+alt+2'):
            print("[Mic recording: STOPPED]")
            isMicRecording = False
            sd.stop()
            elapsedTime = recordedAudioFromMic[
                :int( math.ceil(time.time() - timeOfStartedAudioRecordingFromMic) * sampleRate )
                ]
            sf.write(fileName_micRecorded, elapsedTime, samplerate = sampleRate, format = 'mp3')
            recordedAudioFromMic = None

            current_dir = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(current_dir, fileName_micRecorded)
            dest_dir = os.path.join(current_dir, 'myAudio')
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.copy(file_path, dest_dir)
            os.rename(os.path.join(dest_dir, fileName_micRecorded), os.path.join(dest_dir, str(time.time()) + '.mp3'))

            convertAudioToText(fileName_micRecorded, fileName_micRecordedToText)
            
            text_file = open(fileName_micRecordedToText, "r")
            micRecordedText = text_file.read()
            text_file.close()

            print("User: " + micRecordedText)
            resultOfCheckingGrammar = botik.checkGrammar(micRecordedText)
            if len(resultOfCheckingGrammar) > 10:
                print("AI-corrector: " + resultOfCheckingGrammar)
                synthesizeAudioFromText(resultOfCheckingGrammar, fileName_synthesized)
                playAudio(fileName_synthesized)

                listForSavingConversationInText.append("User: " + micRecordedText)
                listForSavingConversationInText.append("AI-corrector: " + resultOfCheckingGrammar)
            else:
                aiAnswer = botik.chat(micRecordedText)
                print("AI: " + aiAnswer)
                synthesizeAudioFromText(aiAnswer, fileName_synthesized)
                playAudio(fileName_synthesized)

                listForSavingConversationInText.append("User: " + micRecordedText)
                listForSavingConversationInText.append("AI: " + aiAnswer)
        
        if isMicRecording and keyboard.is_pressed('shift+alt+3'):
            print("[Mic recording: INTERRUPTED]")
            isMicRecording = False
            sd.stop()
            recordedAudioFromMic = None

        if not isMicRecording and keyboard.is_pressed('shift+alt+4'):
            print("[EXIT]")
            with open(f'{time.time()}.txt', "w") as f:
                for string in listForSavingConversationInText:
                    f.write(string + "\n")
            exit()