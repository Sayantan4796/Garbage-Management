# Garbage-Management
The aim of this project is to create a mobile based application, whose task is to manage the wastebins accross the campus.
There are three units to the whole system. Housekeeping unit (client 1 (a separate app)), the institute server (centralised sever), the wastebin carrier unit (client 2 (a separate app)). Housekeeping unit will manually check the wastebins, and when he/she sees that it is full, on his/her smartphoe he/she will open the application and request the carrier unit to fetch it. This communication will be facilitated by the server as a middle-man unit. The carrier or we shall call it the mobile unit will get the request, along wih lat./long. information of the particular wastebin. The mobile unit will be then routed to the watebin to complete the task. The router and the map is being facilitated by the HERE technologies APIs. 


For now, we are focussing ourselves to establish a two client to server connection. The code that we have uploaded is working for one client to server connection. The capability is to have a multiple client support to the server. 

If we do the above mentioned task, then what we will have is basicaaly a chat/messaging application. To elevate it to perform our given objective, we need to send objects instead of strings. But that we will focus on later. And this readme file will get regularly updated.  
