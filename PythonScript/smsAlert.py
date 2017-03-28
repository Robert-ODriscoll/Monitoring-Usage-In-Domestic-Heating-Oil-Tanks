#!/usr/bin/python
#Author: Robert O Driscoll
#This Program is designed to retrieve the last 2 entries of the distance values
# and compare them, If the value is greater than 2 cm 
#then it will call a send sms function that will send a specific message 
#to an assigned number informing the tank owner of the unsual  drop in oil. 
#Once this functionality is complete I will look at sending the values of the tank aswell 
#as the user may be able to make an assumption about the level drop.
#all 

import os
import MySQLdb
from random import randrange
import urllib      # URL functions
import urllib2     # URL functions
import time
import datetime

#########################import libraries
database = MySQLdb.connect(host='#####',user='####',passwd='###',db='######') # link to database

cursor = database.cursor()
#########################set up database connection
message = 'Robert, Your tank has dropped more than 1 litre in the last hour!'
username = ''
sender = '#####'
hash = '######'
numbers = ('#######')
def sendSMS():
        test_flag = 0
        values = {'test'    : test_flag,
                  'uname'   : username,
                  'hash'    : hash,
                  'message' : message,
                  'from'    : sender,
                  'selectednums' : numbers }
        url = 'http://www.txtlocal.com/sendsmspost.php'
        postdata = urllib.urlencode(values)
        req = urllib2.Request(url, postdata)
        print 'Attempt to send SMS ...'
        try:
          response = urllib2.urlopen(req)
          response_url = response.geturl()
          if response_url==url:
            print 'SMS sent!'
        except urllib2.URLError, e:
          print 'Send failed!'
          print e.reason

######################################
#cursor.execute ("SELECT distance FROM projectdata WHERE id = (SELECT MAX(id) FROM projectdata)")
cursor.execute ("SELECT distance FROM projectdata ORDER BY id DESC LIMIT 2")
data = cursor.fetchall ()

row = [item[0] for item in data]
dropVar = row[0] - row[1]



if dropVar >= 2.5:
        #sendSms()
        print "Trouble"
else:
        print "Everything is normal"


cursor.close ()


