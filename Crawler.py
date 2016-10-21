import requests
from bs4 import BeautifulSoup

def getText(a):
	Text = ""
	for each in a:
		Text = Text + " " + each.text.encode("utf-8").strip()
	return Text

a = BeautifulSoup(requests.get("https://www.google.co.in/search?q=MSFT&hl=en&gl=in&as_drrb=b&authuser=0&source=lnt&tbs=cdr%3A1%2Ccd_min%3A10%2F10%2F2011%2Ccd_max%3A10%2F10%2F2011&tbm=nws&&start=0").content, "lxml").select('.r a')
href = []
for each in a:
	href.append(each['href'][7:])

data = [['p', 'span', 'strong', 'b', 'pre', 'summary']]
for each in href:
	tags = []
	soup = BeautifulSoup(requests.get(each).content, "lxml")
	for tag in data[0]:
		tags.append(getText(soup.select(tag)))
	data.append(tags)
print(data)