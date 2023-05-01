import requests
import sounddevice as sd
import soundfile as sf
import openai

import requests
import time

from info import assemblyaiKey

from gtts import gTTS

def synthesizeAudioFromText(text, filename):
    myobj = gTTS(text=text)
    myobj.save(filename)


def playAudio(fileName):
    data, samplerate = sf.read(fileName)
    sd.play(data, samplerate)
    sd.wait()


def _read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data

def convertAudioToText(audioFileName, textFileName):
    audio_file= open(audioFileName, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    f = open(textFileName, "w")
    f.write(transcript.text)


# def convertAudioToText(audioFileName, textFileName):
#     UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
#     TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
    
#     headers = {"authorization": assemblyaiKey, "content-type": "application/json"}

#     upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=_read_file(audioFileName))
#     audio_url = upload_response.json()["upload_url"]

#     transcript_request = {'audio_url': audio_url}
#     transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
#     _id = transcript_response.json()["id"]
    
#     while True:
#         polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)

#         if polling_response.json()['status'] == 'completed':
#             with open(textFileName, 'w') as f:
#                 f.write(polling_response.json()['text'])
#             break
#         elif polling_response.json()['status'] == 'error':
#             raise Exception("Transcription failed. Make sure a valid API key has been used.")
#         else:
#             print("Transcription queued or processing ...")
#             time.sleep(1)

if __name__ == "__main__":
    pass