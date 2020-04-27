import socket


host = socket.gethostname() 
             ############### as both code is running on same pc ###################3
            
port = 5000                       ############# socket server port number################33

client_socket = socket.socket()               ################# initiate the connection ##########e
client_socket.connect((host, port))       ############### connect to the server########################


in_data = client_socket.recv(1024).decode()
   

    
print("From IIT-H server: ", in_data)


data = client_socket.recv(1024).decode()

print("From Housekeeping unit: ", data)

client_socket.close()               ################### closing the connection ######################



