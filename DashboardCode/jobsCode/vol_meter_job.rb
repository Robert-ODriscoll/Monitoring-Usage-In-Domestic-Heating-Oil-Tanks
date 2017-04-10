require 'mysql2'

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

