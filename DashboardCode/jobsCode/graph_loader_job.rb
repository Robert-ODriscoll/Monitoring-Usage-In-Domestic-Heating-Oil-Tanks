require 'mysql2'


SCHEDULER.every '1m', :first_in => 0 do |job|

# Myql connection
  db = Mysql2::Client.new(:host => "******", :username => "****", :password => "*********", :port => 3306, :database => "*******" )
  sql =  "SELECT vol,epoch FROM projectdata"

  results  = db.query(sql)

  values1 = results.map do |row|
   row = {
    :val1 => row['vol']
 }
end
values2 = results.map do |row|
   row = {
    :val2 => row['epoch']
 }
end

array1 = []
array2 = []
array1 = values1.map{|x| x[:val1]}
array2 = values2.map{|x| x[:val2]}

#print(array1)
#print(array2)
points = []
  points << { x: array1, y: array2 }

  send_event('graph', points: points)
end

