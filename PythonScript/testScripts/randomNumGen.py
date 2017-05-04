#!/usr/bin/python
#Author: Robert O Driscoll
#This program has been designed to generate a random variable
#asssign an id and send it to a purpose made database table
#and will assist me in the process of data analysis
#It will be linked to the oil tank animation at a later stage
#For debugging i am printing to a test doc
import MySQLdb
from random import randrange
#########################import libraries
database = MySQLdb.connect(host='********',user='******',passwd$
cursor = database.cursor()
#########################set up database connection
ranNum = randrange(3,24)
comment = "Random Number"
#text_file = open("output.txt", "w")
#text_file.write("Random Number generated is: %s\n " % ranNum)
#text_file.write("Comment: %s\n\n" % comment)
cursor.execute(''' INSERT INTO `randomnum`(`randomint`,comment) VALUES (%s,%s) ''',(ranNum,comment))
database.insert_id()
id = database.insert_id() #store id

#data = cursor.fetchall () #collects all data  from table

text_file = open("output.txt", "w")
text_file.write("Random Number generated is: %s\n " % ranNum)
text_file.write("Comment: %s\n\n" % comment)
text_file.write("ID: %s\n\n" % id)



database.commit()
database.close()
#########################Inserts random number to tabole and commits to database and close connection


