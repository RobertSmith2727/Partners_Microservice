How to programmatically call the program call the function: insert(list) 
The list must contain strings for each attribute in this order: [first_name, last_name, email, bio, password, role]
To get the data back declare a variable like so returnData = insert(list) 
returnData will now contain the SQL query



To use the communication pipe
you will first have to download RabbitMQ node and start it:
Install rabbitmq
command to start rabbitMQ node

link to download and start depenidnon system setup: https://www.rabbitmq.com/download.html

After you have those steps completed, you will need MicroReceiveChan.py and PartnerReceiveChan.py running to be able to listen for message traffic

Then to send a message to the microservice throught the communication pipe, you will call: sendToMicro(list)
The list must contain strings for each attribute in this order: [first_name, last_name, email, bio, password, role]
This data will be sent to the microservice. It will then generate a SQL query and return the query to the partnerReceiveChan() channel.
To use the data, on line 15 of PartnerReceiveChan.py the is a line "# TODO do something here with "body.decode('ascii')"
This is where you wold enter you function to use the SQL query. 

Somehting like this partnersFunction(body.decode('ascii'))
This must be decoded or it will be in ascii text and it will be unusable. Decoding it will charnge it to a string
