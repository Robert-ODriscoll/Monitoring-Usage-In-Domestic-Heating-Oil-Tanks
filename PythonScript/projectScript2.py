import datetime
import Adafruit_DHT
import MySQLdb
import time
import RPi.GPIO as GPIO

#def tempAvg()
#def distanceReading()
#def HumidityAvg()

GPIO.setmode(GPIO.BCM)

triggerPin = 23         ########## declare pin variables
echoPin = 24
humidity, temperature = Adafruit_DHT.read_retry(11, 4)     ######## call adafruit

GPIO.setup(triggerPin,GPIO.OUT)  ####### set triggerPin as output and echoPin as input
GPIO.setup(echoPin,GPIO.IN)

database = MySQLdb.connect(host='localhost',user='root',passwd='root',db='Project_Database')# li$
cursor = database.cursor()

tempList = []  ###### create a few  arrays to store tempreture/humidity/distance readings
humidList = []
#disList = []

epoch = int(time.time()) ###### return epoch value


############## Function returning the distance from the sensor to the closest tempreture
def distanceReading():
        GPIO.output(triggerPin, False)     #### sets trigger low
        time.sleep(5)                      ##### delay for 5 seconds to allow the sensor to cali$

        GPIO.output(triggerPin, True)      ##### sets the trigger high
        time.sleep(0.00001)                #####allow for delay of 0.00001 seconds
        GPIO.output(triggerPin, False)     ######sets the trigger back to low


        while GPIO.input(echoPin)==0:
                lastLowPulse = time.time()
        while GPIO.input(echoPin)==1:
                lastHighPulse = time.time()
                 difference = lastHighPulse - lastLowPulse

        #humidList = [di

        tempdistance = difference * 17150

        distance = round(tempdistance, 2)
        return distance


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

        temperatureAverage = tempAvg()
humidityAverage = HumidityAvg()
tankReading = distanceReading()


cursor.execute(''' INSERT INTO `mySensors`(`epoch`, `temp`,`humidity`,`distance`) VALUES (%s,%s,$

database.commit() ######### commits to database
database.close() ####### close connection


GPIO.cleanup()

