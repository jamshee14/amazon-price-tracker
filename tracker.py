import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
MY_EMAIL=os.getenv("EMAIL_USER")
MY_PASSWORD=os.getenv("EMAIL_PASS")
url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
BUY_PRICE=60.00
def send_alert(price):
    print("price is low logging in to gmail")
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            subject="amazon price alert"
            body=f"the price is now {price}. buy it here{url}"
            msg=f"subject :{subject}\n\n{body}"
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=msg
            )
            print("email sent successfully")
    except Exception as e:
        print(f"error sending email{e}")
def check_price():
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0;Win 64; x64)"}
    response=requests.get(url,headers=header)
    soup=BeautifulSoup(response.content,'html.parser')
    price_tag=soup.find("p",class_="price_color")
    price_text=price_tag.get_text()
    price=float(price_text.replace('£', ''))
    print(f"current price is{price}")
    if price<52:
        send_alert(price)
    else:
        print("product is expensive")
if __name__=="__main__":
    check_price()
