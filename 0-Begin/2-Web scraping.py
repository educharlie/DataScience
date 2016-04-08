url = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"
import requests
from bs4 import BeautifulSoup
html = requests.get(url)
bsObj = BeautifulSoup(html.text)
tables = bsObj.find_all('table')
tables[0].find("th")
print(tables[0])

