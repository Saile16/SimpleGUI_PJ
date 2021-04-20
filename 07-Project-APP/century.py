import requests
from bs4 import BeautifulSoup
r = requests.get(
    "http://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS")
c = r.content
soup = BeautifulSoup(c, "html.parser")
# print(soup)
soup.prettify()
result = soup.find_all("div", {"class": "propertyRow"})
print(len(result))
