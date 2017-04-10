require 'mysql2'

SCHEDULER.every '1m', :first_in => 0 do |job|

# Myql connection
  db = Mysql2::Client.new(:host => "*******", :username => "****", :password => "*****", :port => 3306, :database => "*******" )
  sql =  "SELECT temp FROM projectdata ORDER BY id DESC LIMIT 1"
  results = db.query(sql)

   tempreture = results.map do |row|
   row = {
    :value3 => row['temp']
 }
  end
  tempString = tempreture.join("}")

  varname = tempString.split(/> */)[1]
  newTempreture = varname.chomp("}")
 # print(newTempreture)


 send_event('temp_meter' , {value: newTempreture})
end

