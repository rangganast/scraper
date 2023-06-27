import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")

cards = soup.find("section").find_all("div")[1].find_all("article", {"class": "product_pod"})

links = []
for card in cards:
    link = card.find("h3").find('a').get("href")
    links.append(link)

for link in links:
    link_page = requests.get("http://books.toscrape.com/" + link)
    link_soup = BeautifulSoup(link_page.content, "lxml")
    info_div = link_soup.find("article", {"class": "product_page"})
    
    first_div = info_div.find("div")

    book_title = first_div.find("div", {"class": "product_main"}).find("h1").text
    book_price = first_div.find("div", {"class": "product_main"}).find("p", {"class": "price_color"}).text
    book_desc = info_div.find("div", {"id": "product_description"}).find_next_sibling().text