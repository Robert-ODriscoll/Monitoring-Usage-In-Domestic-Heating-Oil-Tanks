#!/usr/bin/env python
import os
import MySQLdb
import urllib      # URL functions
import urllib2     # URL functions
import time
import datetime
import requests
from bs4 import BeautifulSoup

########################################################################################

#######################################################################################
database = MySQLdb.connect(host='#####',user='#####',passwd='######',db='######') 
cursor = database.cursor()
cursor.execute ("SELECT epoch,vol,temp FROM dailydata ORDER BY id DESC LIMIT 2")
data = cursor.fetchall ()
dailyrow = [item[0] for item in data]
dailyrow2 = [item[1] for item in data]
dailyrow3 = [item[2] for item in data]
dailytemp = dailyrow3[0]
dailyepoch =   datetime.datetime.fromtimestamp(dailyrow[0]).strftime('%c') 
dailylevelVar = dailyrow2[0]
dailydropVar =  dailyrow2[1] - dailylevelVar


###########################################################################################

###########################################################################################
cursor.execute ("SELECT epoch,vol,temp FROM weeklydata ORDER BY id DESC LIMIT 2")
data = cursor.fetchall ()
weeklyrow = [item[0] for item in data]
weeklyrow2 = [item[1] for item in data]
weeklyrow3 = [item[2] for item in data]
weeklytemp = weeklyrow3[0]
weeklyepoch =   datetime.datetime.fromtimestamp(weeklyrow[0]).strftime('%c') 
weeklylevelVar = weeklyrow2[0]
weeklydropVar =  weeklyrow2[1] - weeklylevelVar

dailyhours = (dailyrow[0]-dailyrow[1])/3600
weeklyhours = (weeklyrow[0]-weeklyrow[1])/3600


##########################################################################################

##########################################################################################
url1 = "http://www.cheapestoil.ie/distributors/Mor-Oil?l=7"
url2 = "http://www.cheapestoil.ie/distributors/MacMahon-Oil?l=7"
url3 = "http://www.cheapestoil.ie/heating-oil-prices/Galway"

r1 = requests.get(url1)
r2 = requests.get(url2)
r3 = requests.get(url3)
soup1 = BeautifulSoup(r1.content,"lxml")
soup2 = BeautifulSoup(r2.content,"lxml")
soup3 = BeautifulSoup(r3.content,"lxml")

links1 = soup1.find_all("a")
links2 = soup2.find_all("a")
#links3 = soup3.find_all("a")

oilInfo1 = soup1.find_all("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_Distributorbody_pnlWorking"})
oilInfo2 = soup2.find_all("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_Distributorbody_pnlWorking"})
#oilInfo3 = soup3.find_all("span", {"class": "CellPrice"})

###################################################################################################

###################################################################################################
for item1 in oilInfo1:
        textString1 = item1.text

for item2 in oilInfo2:
        textString2 = item2.text


newString1 = textString1.encode('ascii', 'ignore').decode('ascii')
newString2 = textString2.encode('ascii', 'ignore').decode('ascii')
newString3 = "%.2f Litres, %d Degrees, As of %s,dailyhours,%d" % (dailydropVar,dailytemp,dailyepoch,dailyhours)
newString4 = "%.2f Litres, %d Degrees, As of %s,weeklyhours,%d" % (weeklydropVar,weeklytemp,weeklyepoch,weeklyhours)

################################################################################################

##################################################################################################
text_file1 = open("MorOil.txt", "w")
text_file1.write(newString1)
text_file2 = open("MacMahon.txt", "w")
text_file2.write(newString2)
text_file3 = open("dailyusage.txt", "w")
text_file3.write(newString3)
text_file4 = open("weeklyusage.txt", "w")
text_file4.write(newString4)
text_file1.close()
text_file2.close()
text_file3.close()
text_file4.close()

