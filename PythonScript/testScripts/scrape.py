#Simple test script to utilise the beautiful soup library. I am reading in the entire html doc from the 
#URL provided and saving it as an object and then using .find_all() function to parse out

#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

url = "http://www.cheapestoil.ie/distributors/Mor-Oil?l=7"
r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")

links = soup.find_all("a")

#for link in links:
#	print "<a href='%s'>%s</a>" %(link.get("href"), link.text)


oilInfo = soup.find_all("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_Distributorbody_pnlWorking"})
#vender = soup.find_all("span", {"class": "CellSupplier"})
for item in oilInfo:
	print item.text

#for item2 in vender:
#print item2.text



