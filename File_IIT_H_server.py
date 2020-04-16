import socket
#from threading import Thread

def server_program():
   
    all_connections = []
    all_address = []
   
    host = socket.gethostname()       ###### get the hostname ###########
    port = 5000                   ##################### initiate port no above 1024 ###############
    server_socket = socket.socket()                 ############# initiate the connection ##########e
   
    server_socket.bind((host, port))     ############### bind host address and port together ##############

            ############### configure how many client the server can listen simultaneously ################
    server_socket.listen(5)


    #def accepting_connections():
     #   for c in all_connections:
      #      c.close()

    #del all_connections[:]
    #del all_address[:]

   
    conn, address = server_socket.accept() 
   # socket.setblocking(1)
    all_connections.append(conn)
    all_address.append(address)
    print("Connection from: " + str(address))
    while True:
                                     ################ receive data stream. it won't accept data packet greater than 1024 bytes ###########
        data = conn.recv(1024).decode()
        if not data:
                                        ########### if data is not received break #############
             break
        print("from housekeeping unit: " + str(data))
                # data = input(' -> ')
        conn.send(data.encode())  ########## send data to the client ###########

    conn.close() ############## close the connection ###############


if __name__ == '__main__':
    server_program()
