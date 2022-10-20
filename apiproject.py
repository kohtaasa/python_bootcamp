from pyfiglet import figlet_format
from termcolor import colored
import random
import requests


ascii_art = figlet_format("Dad Joke 3000")
colored_ascii = colored(ascii_art, color="magenta")
print(colored_ascii)

key = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": key}
).json()

results = res['results']
num_results = res['total_jokes']

print(f"I've got {num_results} jokes about {key}. Here's one:")
print(random.choice(results)['joke'])