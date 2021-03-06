#!/usr/bin/python
#Author: Robert O Driscoll
#This Program is designed to retrieve the last 2 entries of the distance values
# and compare them, If the value is greater than 2 cm 
#then it will call a send sms function that will send a specific message 
#to an assigned number informing the tank owner of the unsual  drop in oil. 
#I have also added my leveldetect image script to this script as i optimised it to just a 
#couple of lines. The program now also returns the same messages to a text file that can be read
#into the ruby dashboard accordingly as a sort of alerts feature. This program runs in an hourly 
#cronjob from the aws ec2 linux machine.

import os
import MySQLdb
import urllib      # URL functions
import urllib2     # URL functions
import time
import datetime

database = MySQLdb.connect(host='####',user='######',passwd='#####',db='#######') 
cursor = database.cursor()
#########################set up database connection
message0 = 'Everything is normal'
message1 = 'Dropped more than 3 litre in the last hour!'
message2 = 'You have half a tank of oil left!'
message3 = '5 letres left, its time for a refill'
message4 = 'Your tank is empty!'
############################Set up text local API details and write a couple of duplicate message funtions 
username = '###'
sender = 'oilPI'
hash = '#######'
numbers = ('######')
def sendSMS1():
        test_flag = 0
        values = {'test'    : test_flag,
                  'uname'   : username,
                  'hash'    : hash,
                  'message' : message1,
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

def sendSMS2():
        test_flag = 0
        values = {'test'    : test_flag,
                  'uname'   : username,
                  'hash'    : hash,
                  'message' : message2,
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

def sendSMS3():
        test_flag = 0
        values = {'test'    : test_flag,
                  'uname'   : username,
                  'hash'    : hash,
                  'message' : message3,
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
def sendSMS4():
        test_flag = 0
        values = {'test'    : test_flag,
                  'uname'   : username,
                  'hash'    : hash,
                  'message' : message4,
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

cursor.execute ("SELECT vol FROM projectdata ORDER BY id DESC LIMIT 2") #################### open database and retrieve the last 2 values from the volume column
data = cursor.fetchall ()

row = [item[0] for item in data]

levelVar = row[0]
dropVar =  row[1] - levelVar ####### subtract them to find the drop in oil

os.system('cp /home/ubuntu/AnimationImgs/image/'+ str(int(round(levelVar,0))) +'.png /home/ubuntu/oil_monitor/assets/images/imp$' ############## Copy the level image from one folder to another accourding to the level

#print dropVar
#print levelVar
###############################Afew if statements to compare the different conditions and execute certain tasks depending on the scenario ie. send sms and write alert to text file
if dropVar >= 3:
        sendSMS1()
        text_file = open("Alert.txt", "w")
        text_file.write(message1)
        text_file.close()


else:
        text_file = open("Alert.txt", "w")
        text_file.write(message0)
        text_file.close()


if levelVar >= 14.0 and leveVar <= 15.0:
        sendSMS2()
        text_file = open("Alert.txt", "w")
        text_file.write(message2)
        text_file.close()


elif levelVar >= 5.0 and levelVar <= 6.0: 
        sendSMS3()
        text_file = open("Alert.txt", "w")
        text_file.write(message3)
        text_file.close()

elif levelVar  <= 3.0:
        sendSMS4() 
        text_file = open("Alert.txt", "w")
        text_file.write(message4)
        text_file.close()


cursor.close ()

