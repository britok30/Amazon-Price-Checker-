import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alpha+ilce+7m3+emount&qid=1563942434&s=gateway&sr=8-3"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 2.000):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 2.000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('miamielitebaseball@gmail.com', 'ksgsevczwenmhboz')

    subject = "Price fell down"
    body = "Check the amazon link https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alpha+ilce+7m3+emount&qid=1563942434&s=gateway&sr=8-3"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "miamielitebaseball@gmail.com",
        "britok30@gmail.com",
        msg
    )

    print("HEY EMAIL HAS BEEN SENT")

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 1440)
