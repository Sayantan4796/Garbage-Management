import socket


def client1_program():
    host = socket.gethostname()          ############### as both code is running on same pc ###################3
    port = 5000                       ############# socket server port number################33

    client_socket = socket.socket()               ################# initiate the connection ##########e
    client_socket.connect((host, port))       ############### connect to the server########################
    
    wastebin_attr = open("/Users/sayantanmandal/Python Programs/Waste_data.txt", 'r')  ######### Opening the .txt file ########
    wa = wastebin_attr.read()                                      ############ Reading the .txt file ##################
    

    message = wa      

    client_socket.send(message.encode())        ########## sending the  message from socket point but before encoding in bytes #########

    client_socket.close()               ################### closing the connection ######################

if __name__ == '__main__':
    client1_program()

