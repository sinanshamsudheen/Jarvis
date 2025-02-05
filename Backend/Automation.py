from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os

env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "05uR6d LTK0O", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLaOe",
           "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
client = Groq(api_key=GroqAPIKey)
professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask",
]

messages = []

SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs,poems etc."}]

def GoogleSearch(Topic):
    search(Topic)
    return True

def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})

        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )
        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer

    Topic: str = Topic.replace("Content ", "")
    ContentByAI = ContentWriterAI(Topic)

    with open(rf"Data\{Topic.lower().replace(' ', '')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI)
        file.close()
    OpenNotepad(rf"Data\{Topic.lower().replace(' ', '')}.txt")
    return True

def YoutubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app, sess=requests.session()):
    website_mappings = {
        "facebook": "https://www.facebook.com/",
        "youtube": "https://www.youtube.com/",
        "twitter": "https://twitter.com/",
        "instagram": "https://www.instagram.com/",
        "linkedin": "https://www.linkedin.com/",
        "whatsapp": "https://web.whatsapp.com/",
        "gmail": "https://mail.google.com/",
        "github": "https://github.com/sinanshamsudheen",
        "git": "https://github.com/sinanshamsudheen",
        "repository": "https://github.com/sinanshamsudheen?tab=repositories",
        "ktu": "https://www.ktunotes.in/ktu-s4-cse-notes-2019-scheme/",
        "gfg": "https://www.geeksforgeeks.org/batch/gfg-160-problems?tab=Chapters",
        "amazon": "https://www.amazon.in/",
        "flipkart": "https://www.flipkart.com/"
    }

    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True
    except:
        if app.lower() in website_mappings:
            webopen(website_mappings[app.lower()])
            return True

        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', {'jsname': 'UWckNb'})
            return [link.get('href') for link in links]

        def search_google(query):
            url = f"https://www.google.com/search?q={query}"
            headers = {'User-Agent': useragent}
            response = sess.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                print("Failed to retrieve search results.")
            return None

        html = search_google(app)
        if html:
            links = extract_links(html)
            if links:
                webopen(links[0])
        return True

def CloseApp(app):
    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False

def System(command):
    def mute():
        keyboard.press_and_release("volume mute")
    def unmute():
        keyboard.press_and_release("volume mute")
    def volume_up():
        keyboard.press_and_release("volume up")
    def volume_down():
        keyboard.press_and_release("volume down")

    if command == "mute":
        mute()
    elif command == "unmute":
        unmute()
    elif command == "volume up":
        volume_up()
    elif command == "volume down":
        volume_down()
    return True

async def TranslateAndExecute(commands: list[str]):
    funcs = []

    for command in commands:
        if command.startswith("open "):
            fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
            funcs.append(fun)
        elif command.startswith("content "):
            fun = asyncio.to_thread(Content, command.removeprefix("content "))
            funcs.append(fun)
        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
            funcs.append(fun)
        elif command.lower().startswith("play "):
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
            funcs.append(fun)
        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))
            funcs.append(fun)
        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YoutubeSearch, command.removeprefix("youtube search "))
            funcs.append(fun)
        elif command.startswith("system "):
            fun = asyncio.to_thread(System, command.removeprefix("system "))
            funcs.append(fun)
        else:
            print(f"No function found for: {command}")

    results = await asyncio.gather(*funcs)
    for result in results:
        yield result

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    return True