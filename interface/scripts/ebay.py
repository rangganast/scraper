import requests
from bs4 import BeautifulSoup

def ebay(query: str):
    query = query.replace(" ", "+")

    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={query}&_sacat=0"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml")

    main_div = soup.find("div", {"id" : "srp-river-results"})
    items = main_div.find_all("li", {"class": "s-item s-item__pl-on-bottom"})

    for item in items:
        image_link = item.find("div", {"class": "s-item__image-wrapper image-treatment"}).find("img", src=True)
        product_title = item.find("div", {"class": "s-item__title"}).text
        product_price = item.find("div", {"class": "s-item__detail--primary"}).text
        try:
            seller = item.find("span", {"class": "s-item__authorized-seller"}).find("span", {"class": "BOLD"}).text
        except:
            seller = "Seller Unknown"

        print(product_title)
        print(product_price)
        print(seller)
        print(image_link['src'])
        print("\n")

    return "success"