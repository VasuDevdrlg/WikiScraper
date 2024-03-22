import requests
from bs4 import BeautifulSoup
def searchwikipedia(key):
      url = f"https://en.wikipedia.org/w/index.php?search={key}&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
      response = requests.get(url)
      soup = BeautifulSoup(response.content, "html.parser")
      first = soup.find('div', class_="mw-search-result-heading")
      prompt=first.a["href"]
      url = f"https://en.wikipedia.org{prompt}"
      return url

    