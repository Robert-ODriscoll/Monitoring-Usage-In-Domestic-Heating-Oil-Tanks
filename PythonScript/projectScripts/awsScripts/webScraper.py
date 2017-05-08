#Author: Robert O Driscoll
#This program is running in an hourly cronjob on my aws ec2 linux machine
#
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
#Opens database connetion and reads from daily reading table. The program reads the last 
#2 values from the epoch, volume and tempreture column and returns them. Using the 
#datetime.datetime.fromtimestamp()function and returns the formatted date and time from the 
#epoch. it subtracts the last 2 values from the volume table and returns the ammount to give the 
#user an idea of how much oil was used that day, and it returns the tempreture from that time 
#aswell. 
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
#This code block does the same as above however it reads from the weekly table to give the user
#an idea of the statistics on a weekly basis 
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
#Here we read in 2 seperate webpages and parse out the content needed by locating the nessasary 
#tags. 
##########################################################################################
url1 = "http://www.cheapestoil.ie/distributors/Mor-Oil?l=7"
url2 = "http://www.cheapestoil.ie/distributors/MacMahon-Oil?l=7"
#url3 = "http://www.cheapestoil.ie/heating-ces/Galway"
r1 = requests.get(url1)
r2 = requests.get(url2)
#r3 = requests.get(url3)
soup1 = BeautifulSoup(r1.content,"lxml")
soup2 = BeautifulSoup(r2.content,"lxml")
#soup3 = BeautifulSoup(r3.content,"lxml")

links1 = soup1.find_all("a")
links2 = soup2.find_all("a")
#links3 = soup3.find_all("a")

oilInfo1 = soup1.find_all("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_Distributorbody_pnlWorking"})
oilInfo2 = soup2.find_all("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_Distributorbody_pnlWorking"})
#oilInfo3 = soup3.find_all("span", {"class": "CellPrice"})

###################################################################################################
#Then we use for loops to read through the text and save to string, as there were some special characters
#from the irish letters in the oil companys names i attempted to parse them out using the
#.encode('ascii', 'ignore').decode('ascii') function. I also created 2 other strings and loaded them with 
#the values taken from the database reults above. 
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
#I then opened a couple of text files and wrote the values to them an closed them.
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

