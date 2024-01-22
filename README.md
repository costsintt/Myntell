# Myntell

## How to use it without writing new code?
If you're planning to use my OpenAI API wrappers, you'll need an OpenAI API key (obviously). Just create a file named 'apiKeys.py' in the project root directory and add the following line:
`apiKeys = ("yourKey")`
If you have multiple API keys (which is a bit odd...), you can add them all! Like this:
`apiKeys = ("key1", "key2", and so on)`

Let's define the terms 'bot' and 'scenario.' A bot refers to a Python object that receives an input string, analyzes it using a specified chat AI API, and returns a string as an answer. Bots have memory and specified behaviours.
A scenario is also a Python object. It takes an input string, analyzes it using multiple bots or any functionality you have programmed into it, and produces a string answer.

Let's examine the pre-coded example (which will be activated as the default behavior of the program if you haven't modified the code). This example will also clarify the unclear purpose of the scenarios.
In the scenario of the default code, we have a bot programmed to respond to input messages with the instruction, 'Pretend you are an arrogant professor hurrying home...' (lol). This scenario outputs the bot's response. Additionally, there's a second bot designed to predict your message (I thought it would be useful...). The message predicted by this second bot is then included in additional information, accessible to the external code. The external code can then synthesize the answer text (of the arrogant professor) and, simultaneously, display the additional information in the terminal (what you might say).

How can a human input a message? In the default code, you can press and hold the right shift button to record your voice, and then release it when you're finished. See the file "interface_user.py".
