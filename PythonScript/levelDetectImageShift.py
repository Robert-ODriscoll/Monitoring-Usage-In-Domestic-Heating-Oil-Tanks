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
database = MySQLdb.connect(host='############',user='####',passwd='####',db='####') # link to database

cursor = database.cursor()
#########################set up database connection

cursor.execute ("SELECT distance FROM projectdata WHERE id = (SELECT MAX(id) FROM projectdata)")

data = cursor.fetchall ()

for row in data :
        levelVar = row[0]

print levelVar

if levelVar <= 2:
        os.system('cp /home/ubuntu/AnimationImg/images/one.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 4:
        os.system('cp /home/ubuntu/AnimationImg/images/two.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 6:
        os.system('cp /home/ubuntu/AnimationImg/images/three.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 8:
        os.system('cp /home/ubuntu/AnimationImg/images/four.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 10:
        os.system('cp /home/ubuntu/AnimationImg/images/five.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 12:
        os.system('cp /home/ubuntu/AnimationImg/images/six.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 14:
        os.system('cp /home/ubuntu/AnimationImg/images/seven.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 16:
        os.system('cp /home/ubuntu/AnimationImg/images/eight.png /home/ubuntu/oiltankmonitord/assets/images/importImage.png')

elif levelVar <= 18:
        os.system('cp /home/ubuntu/AnimationImg/images/nine.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 20:
        os.system('cp /home/ubuntu/AnimationImg/images/ten.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

elif levelVar <= 22:
        os.system('cp /home/ubuntu/AnimationImg/images/eleven.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')
elif levelVar <= 25:
        os.system('cp /home/ubuntu/AnimationImg/images/twenty.png /home/ubuntu/oiltankmonitor/assets/images/importImage.png')

cursor.close ()

