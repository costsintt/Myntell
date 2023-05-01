import openai
from collections import deque

openai.api_key = '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'

class Chatbot:
    def __init__(self, model="gpt-3.5-turbo", messages=[]):
        self.model = model
        self.messages = deque(messages, maxlen=5)  # deque with max length 5 to remember last 5 messages
        self.myRules = {"role": "user", "content": "Be a humorous companion and improvise entertaining responses, even if you lack knowledge on a subject."}

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
          model=self.model,
          messages= [self.myRules] + [mes for mes in self.messages]
        )

        self.messages.append({"role": "assistant", "content": response.choices[0].message['content']})
        
        return response.choices[0].message['content']
    
    def checkGrammar(self, message):

        response = openai.ChatCompletion.create(
          model=self.model,
          messages=[
        {"role": "user",
         "content": f'Check the transcribed audio input for speech errors, including\
                      incorrect sentence formation, missing or incorrect prepositions, and any\
                      other speech and logical errors. If the sentence is correct, output "Correct."\
                      If the sentence is incorrect, provide an explanation\
                      for each problem found. The message: "{message}".'},
                    ]
        )
        
        return response.choices[0].message['content']

if __name__ == "__main__":
    botik = Chatbot()
    print(botik.checkGrammar("I just sit and doing some stuff."))
