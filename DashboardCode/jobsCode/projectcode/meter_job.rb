require 'mysql2'

SCHEDULER.every '1m', :first_in => 0 do |job|

db = Mysql2::Client.new(:host => "localhost", :username => "root", :password => "Clifden@1", :port => 3306, :database => "project" )
sql =  "SELECT humidity,vol,temp FROM projectdata ORDER BY id DESC LIMIT 1"
results = db.query(sql)

temphumidity = results.map do |row|
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
end
string1 = temphumidity.join("}")
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

send_event('vol_meter' , {value: newvol})
send_event('temp_meter' , {value: newtemp})
send_event('hum_meter' , {value: newhumidity})
end

