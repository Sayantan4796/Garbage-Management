import socket
import threading

######## For this project the current code suffices. But more functionality can be added with the inclusion of Queue module #######

class ClientThread(threading.Thread):       
   def __init__(self,conn,Address):
       threading.Thread.__init__(self)
       self.conn = conn
       print("New connection added", Address)
   def run(self):
       self.conn.send(bytes("You are connected to IIT H",'utf-8'))


class RecieveThread(threading.Thread):       
   def __init__(self,conn,Address):               
      threading.Thread.__init__(self)
      self.conn = conn
   def run(self):
       global data
       data = self.conn.recv(1024).decode()
       print("The wastebin attributes are:  ",  data)


class SendThread(threading.Thread):
   def __init__(self,conn,Address):
       threading.Thread.__init__(self)   
       self.conn = conn
   def run(self):
       print("Sending this data to mobile unit")
       self.conn.send(data.encode())


host = ''          
port = 5000              
server_socket = socket.socket()               
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_socket.bind((host, port))   


print("The IIT-H server is active")
print("Waiting for clients to connect")   

while True:
 server_socket.listen(4)     
 conn, Address = server_socket.accept() 
 ClientThread(conn,Address).start()    

 RecieveThread(conn,Address).start()  

 SendThread(conn,Address).start()   
   

 
