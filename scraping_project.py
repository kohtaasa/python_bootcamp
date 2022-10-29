import requests
from bs4 import BeautifulSoup

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

all_quotes = []
res = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(res.text, "html.parser")
quotes = soup.find_all(class_="quote")
for quote in quotes:
    all_quotes.append({
        "text": quote.find(class_="text").get_text(),
        "author": quote.find(class_='author').get_text(),
        "bio_link": quote.find("a")["href"]
    })
