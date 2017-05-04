require 'mysql2'

SCHEDULER.every '1m', :first_in => 0 do |job|

# Myql connection
 
  db = Mysql2::Client.new(:host => "*********", :username => "********", :password => "***********", :port => 3306, :database => "**********" )
  sql =  "SELECT humidity FROM projectdata ORDER BY id DESC LIMIT 1"
  results = db.query(sql)

   humidity = results.map do |row|
   row = {
    :value => row['humidity']
 }
  end
  humString = humidity.join("}")

  varname = humString.split(/> */)[1]
  newhumidity = varname.chomp("}")

 send_event('hum_meter' , {value: newhumidity})
end

