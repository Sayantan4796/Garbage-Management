import socket
import threading
import time

######## For this project the current code suffices. But more functionality can be added with the inclusion of Queue module #######

class ClientThread(threading.Thread):        ############ this thread manages the client connections ############
   def __init__(self,conn,Address):
       threading.Thread.__init__(self)
       self.conn = conn
       print("New connection added", Address)
   def run(self):
       #print ("Connection from : ", Address)
       self.conn.send(bytes("You are connected to IIT H",'utf-8'))


class RecieveThread(threading.Thread):       ############# this thread takes care about recieving the contents of the .txt file 
   def __init__(self,conn,Address):                 ##      from #######  Client_1 ###########################
      threading.Thread.__init__(self)
      self.conn = conn
   def run(self):
       global data
       #print("This data is from Housekeeping unit: ",Address)
       data = self.conn.recv(1024).decode()
       print("The wastebin attributes are:  ",  data)


class SendThread(threading.Thread):
   def __init__(self,conn,Address):
       threading.Thread.__init__(self)      ##### This thread takes care about sending the the recieved contents to ## Client_2 #####
       self.conn = conn
   def run(self):
       print("Sending this data to mobile unit")
       self.conn.send(data.encode())
#############################################################################################################
################################## Main program starts from here ############################################
#############################################################################################################

host = ''    #########  Getting the hostname #######      
port = 5000                ###### Fixing the port ##########
server_socket = socket.socket()                ######### initiate the socket #########
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) ###### Allows to bind to exacly the same port and IP address#####
server_socket.bind((host, port))   ###### binding the host and the port #######


print("The IIT-H server is active")
print("Waiting for clients to connect")   

while True:
 server_socket.listen(4) ########### Allows the server to only allow 4 new clients to be waiting to connect ############    
 conn, Address = server_socket.accept() ### accepting the connections ###### 
 ClientThread(conn,Address).start()    ##### Calling the first thread class #####
 time.sleep(5)
 RecieveThread(conn,Address).start()   ###### Calling the second thread class ######## 
 time.sleep(5)
 SendThread(conn,Address).start() ###### Calling the third thread classs ##########  
   

#conn.close()       #### closing the connection ######## For this project you may not this line, but its inclusion will make the server stop operating                                      provided that you have erased line 49 
