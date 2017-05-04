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

