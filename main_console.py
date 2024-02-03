import requests
from colorama import Fore, Back, Style, init
import os
# Initialize colorama
init()
import random
import yaml

# Load keys from config.yml
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)
OPENAI_API_KEY = cfg['openai_api_key']
user = cfg['user_name']
host = cfg['host']

max_tokens = 1024
min_p = 0.9
top_k = 1
top_p = 0.9
temperature = 0.8
inst_beg = "[INST]"
inst_end = "[/INST]"
chat_history = ''
os.system('cls' if os.name == 'nt' else 'clear')
print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + "*" * 50 + Fore.RESET + Back.RESET + Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + "*" * 50 + Fore.RESET + Back.RESET + Style.RESET_ALL)
print(Fore.CYAN + "Welcome to "+user+"'s chat console!" + Fore.RESET)
print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + "=" * 50 + Fore.RESET + Back.RESET + Style.RESET_ALL)
while True:
    user_input = input(Fore.GREEN + "User: " + Fore.RESET)
    if user_input == 'exit':
        break
    elif user_input == 'clear':
        chat_history = ''
        continue
    prompt = chat_history + f"{inst_beg}{user_input}{inst_end}"
    payload = {
        "prompt": prompt,
        "model": "gpt-3.5-turbo-instruct",
        "max_tokens": max_tokens,
        "n_predict": max_tokens,
        "min_p": min_p,
        "stream": False,
        "seed": random.randint(
            1000002406736107, 3778562406736107
        ),  # Was acting weird without this
        "top_k": top_k,
        "top_p": top_p,
        "stop": ["</s>", inst_beg, inst_end],
        "temperature": temperature,
    }

    response = requests.post(
        host,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
        json=payload,
        timeout=360,
        stream=False,
    )
    if response.status_code == 200:
        answer = response.json()['choices'][0]['text']
        print(Fore.CYAN + "Bot:", answer + Fore.RESET)
        chat_history += f"{inst_beg}{user_input}{inst_end}{answer}"
    else:
        print("Error:", response.status_code)
    print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + "=" * 50 + Fore.RESET + Back.RESET + Style.RESET_ALL)


