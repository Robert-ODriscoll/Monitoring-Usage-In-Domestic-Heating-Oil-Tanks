#!/usr/bin/python
#Author: Robert O Driscoll
#This program has been designed to fetch the last id number in the 
#asssigned database. The depending on the value, send and overite an
#image from one folder to another Via a linux command.
#For now this can be run in a chron job and will simulate the rise and 
#fall of the tank as the value  fetched changes.
#initially the values will be taken from the random number database.
#For debugging i am printing to a test doc

import os
import MySQLdb
from random import randrange
#########################import libraries
database = MySQLdb.connect(host='*********',user='******',passwd$

cursor = database.cursor()
#########################set up database connection

cursor.execute ("SELECT randomint FROM randomnum WHERE id = (SELECT MAX(id) FROM randomnum)")

data = cursor.fetchall ()

for row in data :
        levelVar = row[0]

print levelVar

if levelVar <= 2:
        os.system('cp /home/ubuntu/AnimationImg/one.png /home/ubuntu/oil_monitor_dashboard/assets/im$

elif levelVar <= 4:
        os.system('cp /home/ubuntu/AnimationImg/two.png /home/ubuntu/oil_monitor_dashboard/assets/im$

elif levelVar <= 6:
        os.system('cp /home/ubuntu/AnimationImg/three.png /home/ubuntu/oil_monitor_dashboard/assets/$

elif levelVar <= 8:
        os.system('cp /home/ubuntu/AnimationImg/four.png /home/ubuntu/oil_monitor_dashboard/assets/i$

elif levelVar <= 10:
        os.system('cp /home/ubuntu/AnimationImg/five.png /home/ubuntu/oil_monitor_dashboard/assets/i$

elif levelVar <= 12:
        os.system('cp /home/ubuntu/AnimationImg/six.png /home/ubuntu/oil_monitor_dashboard/assets/im$

elif levelVar <= 14:
        os.system('cp /home/ubuntu/AnimationImg/seven.png /home/ubuntu/oil_monitor_dashboard/assets/$

elif levelVar <= 16:
        os.system('cp /home/ubuntu/AnimationImg/eight.png /home/ubuntu/oil_monitor_dashboard/assets/$

elif levelVar <= 18:
        os.system('cp /home/ubuntu/AnimationImg/nine.png /home/ubuntu/oil_monitor_dashboard/assets/i$

elif levelVar <= 20:
        os.system('cp /home/ubuntu/AnimationImg/ten.png /home/ubuntu/oil_monitor_dashboard/assets/im$

elif levelVar <= 22:
        os.system('cp /home/ubuntu/AnimationImg/eleven.png /home/ubuntu/oil_monitor_dashboard/assets$

elif levelVar <= 24:
        os.system('cp /home/ubuntu/AnimationImg/twelve.png /home/ubuntu/oil_monitor_dashboard/assets$
cursor.close ()



