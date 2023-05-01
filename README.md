# my_voice_assistant

## How does it work?
You need an OpenAI API key. Manually add it to the code.

Press "Alt+Shift+F1" to start recording your microphone.

Press "Alt+Shift+F2" to stop recording, and the recording will be transcribed using the Whisper API.

The transcription will then be checked for speech mistakes using GPT-3.5-Turbo.
  If the AI detects any speech mistakes, it will correct them.
  If the AI does not detect any mistakes, it will respond to your spoken message in a funny way.

All responses from the AI are voiced by using gTTS.

Additionally, your entire conversation will be recorded and saved as a text file, and all of your microphone recording files will also be saved.

Press "Alt+Shift+F3" to stop recording and delete it immediately.
Press "Alt+Shift+F4" to exit the program. 
Before exiting, your conversation will be saved into a file.

## TODO:
1. Clean up the mess and make the code look good.
2. Make it easy to change AI models and APIs in the code.
