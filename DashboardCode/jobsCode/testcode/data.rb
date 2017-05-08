/
Robert O Driscoll
data.rb
This is my first ruby Job Script fro retrieveing data from 
database and map to a correspoding widget in dashing
test code blocks
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


 :label => row['epoch']

<h1 class="title" data-bind="title"></h1>

<ol>
  <li data-foreach-item="items">
    <span class="label1" data-bind="item.label1"></span>
    <span class="value1" data-bind="item.value1"></span>
    <span class="label2" data-bind="item.label2"></span>
    <span class="value2" data-bind="item.value2"></span>
    <span class="label3" data-bind="item.label3"></span>
    <span class="value3" data-bind="item.value3"></span>
  </li>
</ol>

<ul class="list-nostyle">
  <li data-foreach-item="items">
    <span class="label1" data-bind="item.label1"></span>
    <span class="value1" data-bind="item.value1"></span>
    <span class="label2" data-bind="item.label2"></span>
    <span class="value2" data-bind="item.value2"></span>
    <span class="label3" data-bind="item.label3"></span>
    <span class="value3" data-bind="item.value3"></span>
  </li>
</ul>


<p class="more-info" data-bind="moreinfo"></p>
<p class="updated-at" data-bind="updatedAtMessage"></p>

:value1 => row['distance'],
      :label1 => row['Distance:'],
      :value2 => row['epoch'],
      :label2 => row['Epoch Time:'],
      :value3 => row['temp'],
      :label3 => row['Tempreture:']

<h1 class="title" data-bind="title"></h1>

<ol>
  <li data-foreach-item="items">
    <span class="label1" data-bind="item.label1"></span>
    <span class="value1" data-bind="item.value1"></span>
</li>
    <li data-foreach-item="items">
    <span class="label2" data-bind="item.label2"></span>
    <span class="value2" data-bind="item.value2"></span>
</li>
    <li data-foreach-item="items">
    <span class="label3" data-bind="item.label3"></span>
    <span class="value3" data-bind="item.value3"></span>
  </li>
</ol>
<ul class="list-nostyle">
  <li data-foreach-item="items">
    <span class="label1" data-bind="item.label1"></span>
    <span class="value1" data-bind="item.value1"></span>
</li>
    <li data-foreach-item="items">
    <span class="label2" data-bind="item.label2"></span>
    <span class="value2" data-bind="item.value2"></span>
</li>
    <li data-foreach-item="items">
    <span class="label3" data-bind="item.label3"></span>
    <span class="value3" data-bind="item.value3"></span>
 </li>
</ul>
<p class="more-info" data-bind="moreinfo"></p>
<p class="updated-at" data-bind="updatedAtMessage"></p>



databaseItems = results.map do |row|
    row = {

      :value1 => row['distance'],
      :value2 => row['epoch'],
      :value3 => row['temp'],

    }
  end

  send_event('graphdata' , {items:databaseItems})
end






