#Author: Robert O Driscoll
#This program connects to the database and retieves the last three values in the 'distance' , 'epoch' and 'temp ' tables.
#I use foo.map to run through thes lists and return the values. Using js batman databind method to send the data to 
#the oil_monitor.erb  The code is running in another loop that updates every 15 mins powered by a rufus shedular.

require 'mysql2'
SCHEDULER.every '15m', :first_in => 0 do |job|


# Myql connection
  db = Mysql2::Client.new(:host => "**************", :username => "**", :password => "******", :port => 3306, :database => "******" )
  sql =  "SELECT distance,epoch,temp FROM projectdata ORDER BY id DESC LIMIT 1"
  results = db.query(sql)

  databaseItems = results.map do |row|
    row = {

      :value1 => row['distance'],
      :value2 => row['epoch'],
      :value3 => row['temp'],

    }
  end

  send_event('graphdata' , {items:databaseItems})
end

