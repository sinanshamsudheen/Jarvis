from groq import Grop
from json import load,dump
import datetime
from dotenv import dotenv_values

env_vars=dotenv_values(".env")

Username=env_vars.get("Username")
Assistantname=env_vars.get("Assistantname")
GroqAPIKey=env_vars.get("GroqAPIKey")

client=Groq(api_key=GroqAPIKey)

messages=[]

System=""""""

SystemChatBot=[
    {"role":"system","content":System}
]
try:
    with open(r"Data\Chatlog.json","r") as f:
        messages=load(f)
except FileNotFoundError:
    with open(r"Data\Chatlog.json","w") as f:
        dump([],f)

def RealtimeInformation():
    current_date_time=datetime.datetime.now()
    day=current_date_time.strftime("%A")
    date=current_date_time.strftime("%d")
    month=current_date_time.strftime("%B")
    year=current_date_time.strftime("%Y")
    hour=current_date_time.strftime("%H")
    minute=current_date_time.strftime("%M")
    second=current_date_time.strftime("%S")

    data=f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours: {minute} minutes: {second} seconds.\n"
    return data

def AnswerModifier(Answer):
    lines=Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer= '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):