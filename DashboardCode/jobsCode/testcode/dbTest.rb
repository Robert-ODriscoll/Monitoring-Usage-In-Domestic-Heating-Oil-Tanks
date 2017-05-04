require 'mysql2'

# Myql connection

  db = Mysql2::Client.new(:host => "localhost", :username => "root", :password => "Clifden@1", :port => 3306, :database => "project" )
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
print(newhumidity)

