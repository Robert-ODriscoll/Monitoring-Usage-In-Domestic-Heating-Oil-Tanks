!/usr/bin/python
#Author: Robert O Driscoll
#This program has been designed to fetch the last id number in the 
#asssigned database. The depending on the value, send and overite an
#image from one folder to another Via a linux command.
#This program is an improvement on the last in the sense that i have optimised the ammount of 
#code needed to complete the task 

import os
import MySQLdb
from random import randrange
#########################import libraries
database = MySQLdb.connect(host='ec2-34-248-47-124.eu-west-1.compute.amazonaws.com',user='pi',passwd='######',db='######

cursor = database.cursor()
#########################set up database connection

cursor.execute ("SELECT randomint FROM randomnum WHERE id = (SELECT MAX(id) FROM randomnum)")

data = cursor.fetchall ()

for row in data :
        levelVar = row[0]

print levelVar

os.system('cp /home/ubuntu/AnimationImg/images/num/'+ str(int(round(levelVar,0))) +'.png /home/ubuntu/oil_monitor_dashboard$



cursor.close ()

