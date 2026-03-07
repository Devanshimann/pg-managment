import requests
import time
from fake_useragent import UserAgent


url="https://www.magicbricks.com/pg-in-jaipur-pppfr"
session=requests.Session()

headers={
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}
# proxies = {
#     "http": "http://IP:PORT",
#     "https": "http://IP:PORT"
# }
r=session.get(url,headers=headers)
with open("file.html","w",encoding="utf-8")as f:
    f.write(r.text)
