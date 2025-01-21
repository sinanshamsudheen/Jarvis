import cohere
from rich import print
from dotenv import dotenv_values

env_vars=dotenv_values(".env")

cohereAPIKey = env_vars.get("CohereAPIKey")

co=cohere.Client(api_key=CohereAPIKey)

funcs=[
    "exit","general","realtime","open","close","play",
    "generate image","system","content","google search",
    "youtube search","reminder"
]
messages= []

preamble=""""""

ChatHistory = [
    {"role": "User","message":"how are you?"},
    {"role": "Chatbot","message":"general how are you?"},
    {"role": "User","message":"do you like pizza?"},
    {"role": "Chatbot","message":"general do you like pizza?"},
    {"role": "User","message":"open chrome and tell me about mahatma gandhi."},
    {"role": "Chatbot","message":"open chrome, general tell me about mahatma gandhi"},
    {"role": "User","message":"open chrome and firefox"},
    {"role": "Chatbot","message":"open chrome,open firefox"},
    {"role": "User","message":"what is today's date and by the way remind me that i have a dancing performance on 5th aug at 11pm"},
    {"role": "Chatbot","message":"general what is today's date, reminder 11:00pm 5th aug dancing performance"},
    {"role": "User","message":"chat with me."},
    {"role": "Chatbot","message":"general chat with me."}
]