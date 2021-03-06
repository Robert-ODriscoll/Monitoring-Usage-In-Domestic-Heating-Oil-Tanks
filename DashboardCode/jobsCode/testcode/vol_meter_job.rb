#Author: Robert O Driscoll
#Small database program to connect to my database on the aws ec2 linux machine, the program connects to the database
#returns the last value entered in the vol column. foo.mp allows you to run through the element and return a hash map value.
#I then use .join() , .split() and .chomp() TO parse out the value and save it to a string and print it. this is different because I
#have used a schedular and am sending the data to the oil_monitor.erb file.require 'mysql2'

SCHEDULER.every '1m', :first_in => 0 do |job|

# Myql connection
  db = Mysql2::Client.new(:host => "*****", :username => "******", :password => "******", :port => 3306, :database => "********" )
  sql =  "SELECT vol FROM projectdata ORDER BY id DESC LIMIT 1"
  results = db.query(sql)

   volume = results.map do |row|
   row = {
    :value => row['vol']
 }
  end
  volString = volume.join("}")

  varname = volString.split(/> */)[1]
  newVolume = varname.chomp("}")

 send_event('vol_meter' , {value: newVolume})
end

