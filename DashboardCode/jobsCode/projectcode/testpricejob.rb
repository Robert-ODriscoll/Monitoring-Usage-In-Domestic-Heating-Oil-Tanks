#Author: Robert O Driscoll
#This program handles all the reading from textfiles and sends them to their corresponding text widgets
#require 'colorize' ###### not used text colour gem
SCHEDULER.every '20s' do ####### Set up Rufus schedular for every 20s
list1 = [] ########## Declare a few variables
list2 = []
avpricelist1 = []
avpricelist2 = []
pricelist1 = []
pricelist2 = []
str1 = String.new()
str2 = String.new()
string1 = String.new()
string2 = String.new()


nameString = String.new("Name: ")
emailString = String.new("Email: ")
name1 = String.new()
name2 = String.new()
lineBreak = String.new("<br />") ####### as the text will be dispayed using html i used the Raw filter in the text.html file to create new lines in the text
email1 = String.new()
email2 = String.new()
costString1 = String.new("Daily: ")
costString2 = String.new("Yesterday: ")
costString3 = String.new("Weekly: ")
costString4=  String.new("LastWeek: ")
cents = String.new("c")
phone1 = String.new()
phone2 = String.new()

smallprice1 = String.new()
smallprice2 = String.new()
bigprice1 = String.new()
bigprice2 = String.new()


string1 = IO.read('/home/ubuntu/pythonScripts/MorOil.txt') ########### read in text files 
string2 = IO.read('/home/ubuntu/pythonScripts/MacMahon.txt')
pricestring1 = IO.read('/home/ubuntu/pythonScripts/dailyusage.txt')
pricestring2 = IO.read('/home/ubuntu/pythonScripts/weeklyusage.txt')
alertstring = IO.read('/home/ubuntu/pythonScripts/Alert.txt')

str1 = string1.gsub(/\n+|\r+/, "\n").squeeze("\n").strip ######### String manipulation using different ruby string methods to prepare the text in the desired format
str2 = string2.gsub(/\n+|\r+/, "\n").squeeze("\n").strip

list1 = str1.split("\n")
list2 = str2.split("\n")

pricelist1 = pricestring1.split(",")
pricelist2 = pricestring2.split(",")

avpricelist1 = string1.split()
avpricelist2 = string2.split()

tempprice1 = avpricelist1[18] ### locate and extract required array elements 
tempprice2 = avpricelist1[25]
tempprice3 = avpricelist2[20]
tempprice4 = avpricelist2[27]

price1 = tempprice1.chomp("c").to_f ### variable casting string to float
price2 = tempprice2.chomp("c").to_f
price3 = tempprice3.chomp("c").to_f
price4 = tempprice4.chomp("c").to_f
tempdailylitres =  pricelist1[0]
tempweeklylitres = pricelist2[0]

dailylitres = tempdailylitres.chomp(" Litres").to_f
weeklylitres = tempweeklylitres.chomp(" Litres").to_f
tempavPricePerLitre500 = (price1+price3)/2
tempavPricePerLitre1000 = (price2+price4)/2


avPricePerLitre500daily = (dailylitres*tempavPricePerLitre500).to_i ##### variable casting string to int 
avPricePerLitre1000daily = (dailylitres*tempavPricePerLitre1000).to_i
avPricePerLitre500weekly = (weeklylitres*tempavPricePerLitre500).to_i
avPricePerLitre1000weekly = (weeklylitres*tempavPricePerLitre1000).to_i


name1 = [nameString,list1[0]].join()#.blue
name2 = [nameString,list2[0]].join()#.blue
email1 = [emailString,list1[1]].join()#.red
email2 = [emailString,list2[1]].join()#.red
phone1 = list1[2]#.green
phone2 = list2[2]#.green
smallprice1 = [list1[5],list1[6]].join()#.blue
smallprice2 = [list2[5],list2[6]].join()#.blue
bigprice1 = [list1[8],list1[9]].join()#.red
bigprice2 = [list2[8],list2[9]].join()#.red

finalString1 = [name1,lineBreak,email1,lineBreak,phone1,lineBreak,smallprice1,lineBreak,bigprice1,lineBreak].join() ##### prepare all the final text to be sent to the dashboard
finalString2 = [name2,lineBreak,email2,lineBreak,phone2,lineBreak,smallprice2,lineBreak,bigprice2].join()
finalString = [finalString1,lineBreak,finalString2].join("\n")
pricefinalString1 = [pricelist1[0],lineBreak,pricelist1[1],lineBreak,pricelist1[2]].join()
pricefinalString2 = [pricelist2[0],lineBreak,pricelist2[1],lineBreak,pricelist2[2]].join()
costfinalString =[costString2,lineBreak,avPricePerLitre1000daily,cents,lineBreak,costString4,lineBreak,avPricePerLitre1000weekly,cents].join()

#print(costfinalString)


send_event('welcome' , {text: alertstring}) ##### JS batman databinding to send the text data to the oil_monitor.erb file
send_event('yesterday' , {text:pricefinalString1})
send_event('lastweek' , {text:pricefinalString2})
send_event('moroil' , {text: finalString})
send_event('costs' , {text: costfinalString})
end ###### end

