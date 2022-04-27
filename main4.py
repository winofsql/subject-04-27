import requests, pprint, os
from bs4 import BeautifulSoup

url = ''
html = requests.get(url)
response_content = html.content

soup = BeautifulSoup(response_content, "html.parser")
usd_jpy = soup.find("div",class_="YMlKec fxKbKc" )

print(usd_jpy.text)