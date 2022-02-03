from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://simple.wikipedia.org/wiki/List_of_vegetables"

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"mw-parser-output"})

