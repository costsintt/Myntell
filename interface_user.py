import sounddevice as sd
import soundfile as sf
import numpy as np

from io import BytesIO
from typing import Union, BinaryIO

import pygame
from pynput import keyboard

COMBINATION_ACTIVATE = {keyboard.Key.shift_r}
current_keys = set()
isActivated = 0

scenario = None
keys = None
sttAPI = None
ttsAPI = None


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


pygame.init()
pygame.mixer.init()
recorder = AudioRecorder()

def start():
    def on_press(key):
        global isActivated
        if key in COMBINATION_ACTIVATE and key not in current_keys:
            current_keys.add(key)
            if all(k in current_keys for k in COMBINATION_ACTIVATE) and not isActivated:
                isActivated = 1
                print("Recording started...", sep='')
                recorder.start_recording()

    def on_release(key):
        global isActivated
        try:
            current_keys.remove(key)
            if not all(k in current_keys for k in COMBINATION_ACTIVATE) and isActivated:
                isActivated = 0
                print("STOPPED")
                data = recorder.stop_recording()
                audioFile = BytesIO()
                sf.write(audioFile, data, 44100, format="wav")
                audioFile.seek(0)

                userMessage = sttAPI.transcribe(audioFile)
                print("User:\t", userMessage)

                answer = scenario.answer(userMessage)
                print(answer)
                print(scenario.getAdditionalInfo())

                print("\n\n")

                audioFile.seek(0)
                audioFile.truncate(0)
                audioFile.write(ttsAPI.synthesize(answer))

                audioFile.seek(0)
                file_write(audioFile, "temp.mp3")
                pygame.mixer.music.load("temp.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.music.unload()

                ttsAPI.api_key = keys.get()

        except KeyError:
            pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
