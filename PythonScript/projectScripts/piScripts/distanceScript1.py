#!/usr/bin/python
#Author: Robert O Driscoll
#This program has been designed to return and id, epoch, tempreture, distance, volume, humidiy and tank percentage 
#to the project database. The program is one of three running on cronjobs. this is the hourly script running every hour and
#returning any changes in tank condiditons.  

#include a few libraries 
import datetime
import Adafruit_DHT
import MySQLdb
import time
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)

triggerPin = 23         ########## declare pin variables
echoPin = 24
humidity, temperature = Adafruit_DHT.read_retry(11, 4)     ######## call adafruit

GPIO.setup(triggerPin,GPIO.OUT)  ####### set triggerPin as output and echoPin as input
GPIO.setup(echoPin,GPIO.IN)
database = MySQLdb.connect(host='#####',user='#####',passwd='####',db='######')# link to database
cursor = database.cursor()

tempList = []  ###### create a few  arrays to store tempreture/humidity/distance readings
humidList = []
volumeList = []
distanceList = []

epoch = int(time.time()) ###### return epoch value


############## Function returning the distance from the sensor to the closest tempreture 
def distanceReading():
        GPIO.output(triggerPin, False)     #### sets trigger low
        time.sleep(5)                      ##### delay for 5 seconds to allow the sensor to calibrate a good reading

        GPIO.output(triggerPin, True)      ##### sets the trigger high
        time.sleep(0.00001)                #####allow for delay of 0.00001 seconds
        GPIO.output(triggerPin, False)     ######sets the trigger back to low


        while GPIO.input(echoPin)==0:
                lastLowPulse = time.time()
        while GPIO.input(echoPin)==1:
                lastHighPulse = time.time()

        difference = lastHighPulse - lastLowPulse
        tempdistance = difference * 17150
        return  tempdistance
########### Function returning the average value from 11 humidity readings 
def distanceAvg():
        for ss in range(0,10):
                distanceList = [distanceReading()]
        newdistanceVar = sum(distanceList) / float(len(distanceList))
        return newdistanceVar


tankLength = 40 ######### some tank measurments 
tankDiameter = 31
tankDept = 31 - distanceAvg()
radius = tankDiameter/2
fulltankVolume = ((3.14*tankLength)*pow(radius,2))

############# Function returning the value of the tank, Prototyped on the formula for the volume of a cylinder 
def tankVolume():
        displacedVolume = (tankLength*(pow(radius,2)*(math.acos((radius - tankDept)/radius))-((radius - tankDept)*(math.sqrt((2*radius*tankDept)-pow(tankDept,2))))))

        actualDisplacedVolume = displacedVolume/1000
        return actualDisplacedVolume


########## Function returning the average value from 11 temp readings 
def tempAvg():
        for xx in range(0, 10):

                tempList = [temperature]
        newTempVar = sum(tempList) / float(len(tempList))
        return newTempVar

########### Function returning the average value from 11 humidity readings 
def HumidityAvg():
        for ii in range(0, 10):
                humidList = [humidity]
        newHumidityVar = sum(humidList) / float(len(humidList))
        return newHumidityVar

########### Function returning the average value from 11 Volume readings 
def tankVolumeAvg():
        for jj in range(0, 10):
                volumeList = [tankVolume()]
        newtankVar = sum(volumeList) / float(len(volumeList))
        return newtankVar


#save values into float variables and round of to 1 place of decimal using the python round function
tankVolume = round(tankVolumeAvg(),1) 
temperatureAverage = tempAvg()
humidityAverage = HumidityAvg()
tankReading = round(distanceReading(),1)
volumePercentage = round(((fulltankVolume/100)*tankVolume)/100,1)

#############################################more database stuff
database.insert_id()
id = database.insert_id() #store id
cursor.execute(''' INSERT INTO `projectdata`(`epoch`, `temp`,`humidity`,`distance`,`vol`,`percent`) VALUES (%s,%s,%s,%s,%s,%s) ''',(epoch,temperatureAverage,humidityAverage,tankReading,tankVolume,volumePercentage)) ###### inserts data i$

database.commit() ######### commits to database
database.close() ####### close connection


GPIO.cleanup()

