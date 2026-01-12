import requests
from bs4 import BeautifulSoup
url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
def check_price():
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0;Win 64; x64)"}
    page=requests.get(url,headers=header)
    soup=BeautifulSoup(page.content,'html.parser')
    price_tag=soup.find("p",class_="price_color")
    price_text=price_tag.get_text()
    price=float(price_text.replace('£', ''))
    print(f"current price is{price}")
    if price<52:
        print("product is cheap")
    else:
        print("product is expensive")
if __name__=="__main__":
    check_price()
