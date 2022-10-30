import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

# quotes = []
# authors = []
# born_date = []
# born_location = []
# for page in range(1, 2):
#     url = f"https://quotes.toscrape.com/page/{str(page)}/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     for x in soup.select(".text"):
#         quotes.append(x.get_text())
#
#     for x in soup.select(".author"):
#         authors.append(x.get_text())
#
#     for x in soup.select(".quote"):
#         a_tag = x.find("a")
#         parameter = a_tag["href"]
#         author_url = f"https://quotes.toscrape.com{str(parameter)}"
#         response = requests.get(author_url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         date = soup.find("span", {"class", "author-born-date"})
#         born_date.append(date.get_text())
#         loc = soup.find("span", {"class","author-born-location"})
#         born_location.append(loc.get_text())
#
# data = {'quotes': quotes, 'authors': authors, 'born_date': born_date, 'born_location': born_location}
# print(data)

BASE_URL = "https://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(scraped_quotes):
    quote = choice(scraped_quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio_link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The auther was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name start with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author's last name start with: {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? (y/n)?")
    if again.lower() in ('yes', 'y'):
        print("OK YOU PLAY AGAIN!")
        return start_game(scraped_quotes)
    else:
        print("OK, GOODBYE!")


if __name__ == '__main__':
    quotes = read_quotes("quotes.csv")
    start_game(quotes)
