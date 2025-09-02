import time
from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
response = requests.get("https://www.amazon.com/dp/B0DGFXBFCT/ref=sspa_dk_detail_4?pd_rd_i=B0DGFXBFCT&pd_rd_w=44pyH&content-id=amzn1.sym.85ceacba-39b1-4243-8f28-2e014f9512c7&pf_rd_p=85ceacba-39b1-4243-8f28-2e014f9512c7&pf_rd_r=3CSR8357NYM66NKTH001&pd_rd_wg=RCbpd&pd_rd_r=c44a4311-b660-494e-a731-b67557692a24&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9,fa-AF;q=0.8,fa;q=0.7,ru-RU;q=0.6,ru;q=0.5"})
#wating for two second for loading website
time.sleep(2)

amazone_website = response.text

soup = BeautifulSoup(amazone_website,"html.parser")

data = soup.find_all("span", class_="a-offscreen")

price = data[0]
#For getting exact price
whole_price = price.get_text().lstrip("$")
#compare product price with prefered price

if int(float(whole_price)) < 78 and int(float(whole_price)) > 72:
        msg = EmailMessage()
    msg['Subject'] = 'Daily report '
    msg['From'] = 'yourEmail@gmail.com'
    msg['To'] = 'example@gmail.com' #To whom it will be send
    msg.set_content(
        print(f"The price is now {whole_price}")
    )
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('test276t@gmail.com', 'linx aeqv lvhr iwig')
        smtp.send_message(msg)

print(whole_price)
