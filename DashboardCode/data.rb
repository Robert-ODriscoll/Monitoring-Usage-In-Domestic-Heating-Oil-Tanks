/
Robert O Driscoll
data.rb
This is my first ruby Job Script fro retrieveing data from 
database and map to a correspoding widget in dashing
/

require 'mysql2'

SCHEDULER.every '10m', :first_in => 0 do |job|
  db = Mysql2::Client.new(:host => "#########", :username => "####", :password => "######", :port => 3306, :database => "#############" )

  sql =  "SELECT 'distance', 'epoch' FROM projectdata WHERE id = (SELECT MAX(id) FROM projectdata)"
  results = db.query(sql)

  databaseItems = results.map do |row|
    row = {
      :lable => row['distance'],
      :value => row['epoch']
    }
  end 

  send_event('data' , {items:databaseItems})
end


 
