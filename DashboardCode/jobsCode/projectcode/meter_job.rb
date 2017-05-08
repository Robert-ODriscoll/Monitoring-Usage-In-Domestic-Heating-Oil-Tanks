#Author: Robert O Driscoll
#This program optimises a couple of the test programs and is designed to read parse and return values from
#columns in the hourly database and update every minute

require 'mysql2' #################################import mysql gem

SCHEDULER.every '1m', :first_in => 0 do |job| ################ set up Rufus schedular running every 1 min

db = Mysql2::Client.new(:host => "localhost", :username => "root", :password => "Clifden@1", :port => 3306, :database => "project" ) ######### connect to hourly table on project database
sql =  "SELECT humidity,vol,temp FROM projectdata ORDER BY id DESC LIMIT 1" ################# return last value from 'humidity','vol' and 'temp' columns 
results = db.query(sql) ######## handle prepared statement

temphumidity = results.map do |row| ######### read values from prepared statements using foo.map() this returns the values'humidity','vol' and 'temp as hashmap values.
        row = {
                :value => row['humidity']
        }
end
temptemp = results.map do |row|
        row = {
                :value => row['temp']
        }
end
tempvol = results.map do |row|
        row = {
                :value => row['vol']
        }
end #####
string1 = temphumidity.join("}") ####### parse out the 3 values and save to 3 strings
tempvar1 = string1.split(/> */)[1]
newhumidity = tempvar1.chomp("}")
print(newhumidity)
string2 = tempvol.join("}")
tempvar2 = string2.split(/> */)[1]
newvol = tempvar2.chomp("}")
print(newvol)
string3 = temptemp.join("}")
tempvar3 = string3.split(/> */)[1]
newtemp = tempvar3.chomp("}")
print(newtemp)

send_event('vol_meter' , {value: newvol}) #### using batman databind send to the oil_monitor.erb corresponds to the metre widget 
send_event('temp_meter' , {value: newtemp})
send_event('hum_meter' , {value: newhumidity})
end

