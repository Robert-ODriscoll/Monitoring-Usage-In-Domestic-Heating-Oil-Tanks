
#Author: Robert O Driscoll
#Small database program to connect to my database on the aws ec2 linux machine, the program connects to the database
#returns the last value entered in the humidity table. foo.mp allows you to run through the element and return a hash map value.
#I then use .join() , .split() and .chomp() TO parse out the value and save it to a string and print it.
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

